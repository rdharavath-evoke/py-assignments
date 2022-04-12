from os import system
from django.shortcuts import redirect, render
from matplotlib.style import context
from rest_framework import generics
from .serializers import InvoiceSerializer,CertificateOfAnalysisSerializer,InvoiceSerializerandCoa
from rest_framework import views
from .models import CertificateOfAnalysis, Invoice, deleted_coa
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from utils import Properties,TransactionException
from rest_framework import status
from django.shortcuts import HttpResponse,redirect
from django.db import transaction
from django.views import View
from datetime import datetime,timedelta
from django.db.models import Q
from django.db import transaction
from django.core.paginator import Paginator
from django.conf import settings
import re

class LoadAllInvoices(generics.ListAPIView):
    serializer_class=InvoiceSerializer
    queryset=Invoice.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields ="__all__"
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset,many=True)
        return Response({
           "count":queryset.count(),
           "results":serializer.data
        })
class LoadAllCoas(Properties,generics.ListAPIView):
    serializer_class=CertificateOfAnalysisSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields ="__all__"
    def get_object(self):
        try:
            return Invoice.objects.get(invoice_id=self.invoice_id)
        except Invoice.DoesNotExist:
            return None
    def get_queryset(self):
        return CertificateOfAnalysis.objects.filter(Q(deleted_status=False)|Q(deleted_status=None),invoice_no=self.invoice_obj.invoice_no,po_number=self.invoice_obj.po_number)
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset,many=True)
        return Response({
           "count":queryset.count(),
           "results":serializer.data
        })
    def get(self,request,*args,**kwrgs):
        try:
            self.invoice_id=self.request.query_params.get("invoice_id")
            if self.invoice_id:
                self.invoice_obj=self.get_object()
                if self.invoice_obj:
                    return self.list(request)
                return Response({self.STATUS:self.FAILED,self.DESCRIPTION:self.OBJECT_NOT_FOUND},status=status.HTTP_400_BAD_REQUEST)
            return Response({self.STATUS:self.FAILED,self.DESCRIPTION:"please provide {invoice_id} param"},status=status.HTTP_400_BAD_REQUEST)
        except Exception as exc:
            print(exc)
            return Response({self.STATUS:self.EXCEPTION,self.DESCRIPTION:str(exc)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class UpdateInvoice(View):
    def parse_request_data(self,data):
        self.data=dict()
        for key,value in data.items():
            if key not in ['csrfmiddlewaretoken']:
                self.data[key]=value if value.strip()!=str() else None
    def get_object(self):
        try:
            return Invoice.objects.filter(invoice_id=self.data.get("invoice_id"))
        except Invoice.DoesNotExist:
            return None
    def post(self,request,*args,**kwrgs):
        try:
            self.parse_request_data(request.POST)
            obj=self.get_object()
            del self.data["invoice_id"]
            self.data["edited_on"]=Properties.get_date_time()
            obj.update(**self.data)
            return render(request,"success.html",{"message":"invoice","created":"updated"})
        except Exception as exc:
            print(exc)
            return render(request,"error.html")
class UpdateCoa(UpdateInvoice):
    def get_object(self):
        try:
            return CertificateOfAnalysis.objects.filter(Q(deleted_status=False)|Q(deleted_status=None),certificate_of_analsys_id=self.data.get("certificate_of_analsys_id"))
        except Invoice.DoesNotExist:
            return None
    def post(self,request,*args,**kwrgs):
        try:
            self.parse_request_data(request.POST)
            obj=self.get_object()
            del self.data["certificate_of_analsys_id"]
            self.data["edited_on"]=Properties.get_date_time()
            obj.update(**self.data)
            return render(request,"success.html",{"message":"Coa","created":"updated"})
        except Exception:
            return render(request,"error.html")
class PostCoa(UpdateInvoice):
    def get_object(self):
        try:
            return Invoice.objects.get(invoice_no=self.data.get("invoice_no"))
        except Invoice.DoesNotExist:
            return None
    def post(self,request,*args,**kwrgs):
        try:
            self.parse_request_data(request.POST)
            obj=self.get_object()
            if obj:
                self.data["po_number"]=obj.po_number
                CertificateOfAnalysis(**self.data).save()
                return render(request,"success.html",{"message":"Coa","created":"Created"})
            return render(request,"error_message.html",{"message":"Invoice No Not exist"})
        except Exception as exc:
            print(exc)
            return render(request,"error.html")
    
    

class PostCoaRest(Properties,views.APIView):
    def post(self,*args,**kwrgs):
        try:
            invoice=self.request.data.get("invoice")
            coas=self.request.data.get("coas")
            errors=dict()
            with transaction.atomic():
                invoice_ser_obj=InvoiceSerializer(data=invoice)
                if invoice_ser_obj.is_valid():
                    invoice_ser_obj.save()
                    for coa in coas:
                        coa["po_number"]=invoice.get("po_number")
                        coa_ser_obj=CertificateOfAnalysisSerializer(data=coa)
                        if coa_ser_obj.is_valid():
                            coa_ser_obj.save()
                        else:
                            if errors.get("COA")!=None:
                                errors["COA"].append({"coa":coa,"error":coa_ser_obj.errors})
                            else:
                                errors["COA"]=[{"coa":coa,"error":coa_ser_obj.errors}]
                            raise TransactionException
                else:
                    errors["INVOICE"]={"invoice":invoice,"error":invoice_ser_obj.errors}
                    raise TransactionException
            return Response({self.STATUS:self.SUCCESS},status=status.HTTP_200_OK)
        except TransactionException:
            return Response({self.STATUS:self.FAILED,self.DESCRIPTION:errors},status=status.HTTP_400_BAD_REQUEST)
        except Exception as exc:
            print(exc)
            return Response({self.STATUS:self.EXCEPTION,self.DESCRIPTION:str(exc)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SetStatus(PostCoaRest):
    def get_object(self,id):
        try:
            return Invoice.objects.get(invoice_id=id)
        except Invoice.DoesNotExist:
            return None
    def get_objects(self,ids):
        try:
            return Invoice.objects.filter(invoice_id__in=ids)
        except Invoice.DoesNotExist:
            return None
    def update_dates(self,objs):
        for invoice in objs:
            invoice_date=invoice.invoice_date
            for coa in CertificateOfAnalysis.objects.filter(invoice_no=invoice.invoice_no,po_number=invoice.po_number):
                if coa.date_of_manfacture==None and invoice_date!=None and invoice_date.strip()!=str():
                    coa.date_of_manfacture=invoice_date
                if (coa.date_of_manfacture!=None and coa.date_of_manfacture.strip()!=str()) and (coa.expiry_date==None or coa.expiry_date.strip()==str()) and len(coa.date_of_manfacture.split("/"))==3:
                    exp_date=datetime.strptime(coa.date_of_manfacture,self.date_format)
                    coa.expiry_date=exp_date.replace(year=exp_date.year+1)-timedelta(days=1)
                    coa.expiry_date=coa.expiry_date.strftime(self.date_format)
                coa.save()
    def put(self,request,*args,**kwrgs):
        try:
            status_data=self.request.data
            grn=self.request.data.get("grn")
            bot_comments=self.request.data.get("bot_comments")
            if self.request.data.get("ids[]"):
                ids=self.request.data.getlist("ids[]")
            else:  
                ids=self.request.data.get("ids")
            objs=self.get_objects(ids)
            if objs:
                if "grn" in self.request.data.keys():
                    objs.update(grn=grn,edited_on=Properties.get_date_time())
                elif "bot_comments" in self.request.data.keys():
                    objs.update(bot_comments=bot_comments,edited_on=Properties.get_date_time())
                else:
                    with transaction.atomic():
                        objs.update(status=status_data.get('status'),edited_on=Properties.get_date_time())
                        self.update_dates(objs)
                return Response({self.STATUS:self.SUCCESS},status=status.HTTP_200_OK)
            return Response({self.STATUS:self.FAILED,self.DESCRIPTION:self.OBJECT_NOT_FOUND},status=status.HTTP_400_BAD_REQUEST)
        except Exception as exc:
            return Response({self.STATUS:self.EXCEPTION,self.DESCRIPTION:str(exc)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class LoadInvoice(SetStatus):
    def __init__(self):
        super().__init__()
        self.put=None
        self.post=None
    def get(self,request,id,*args,**kwrgs):
        try:
            obj=self.get_object(id)
            if obj:
                return Response({self.STATUS:self.SUCCESS,self.DATA:InvoiceSerializerandCoa(obj).data},status=status.HTTP_200_OK)
            return Response({self.STATUS:self.FAILED,self.DESCRIPTION:self.OBJECT_NOT_FOUND},status=status.HTTP_400_BAD_REQUEST)
        except Exception as exc:
            return Response({self.STATUS:self.EXCEPTION,self.DESCRIPTION:str(exc)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class LoadPdf(SetStatus):
    def get_path(self, type,id):
        try:
            if type=="COA":
                return CertificateOfAnalysis.objects.get(certificate_of_analsys_id=id).doc_path
            elif type=="invoice":
                return Invoice.objects.get(invoice_id=id).invoice_path
            else:
                return Invoice.objects.get(invoice_id=id).boe_doc_path
        except (Invoice.DoesNotExist,CertificateOfAnalysis.DoesNotExist):
            return None
    def get(self,request,id,type,*args,**kwrgs):
        try:
            obj=self.get_path(type,id)
            if obj:
                with open(obj, 'rb') as fh:
                    response = HttpResponse(fh.read(), content_type='application/pdf')
                    return response
            return Response({self.STATUS:self.FAILED,self.DESCRIPTION:self.OBJECT_NOT_FOUND},status=status.HTTP_400_BAD_REQUEST)
        except Exception as exc:
            return Response({self.STATUS:self.EXCEPTION,self.DESCRIPTION:str(exc)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class DeleteCoa(Properties,views.APIView):
    def get_object(self):
        try:
            return CertificateOfAnalysis.objects.filter(Q(deleted_status=False)|Q(deleted_status=None),certificate_of_analsys_id=self.data.get("certificate_of_analsys_id"))
        except Invoice.DoesNotExist:
            return None
    def delete(self,request,*args,**kwrgs):
        try:
            self.data=self.request.data
            objs=self.get_object()
            if len(objs)!=0:
                objs.update(deleted_status=True)
                return Response({self.STATUS:self.SUCCESS},status=status.HTTP_200_OK)
            return Response({self.STATUS:self.FAILED,self.DESCRIPTION:self.OBJECT_NOT_FOUND},status=status.HTTP_400_BAD_REQUEST)
        except Exception as exc:
            return Response({self.STATUS:self.EXCEPTION,self.DESCRIPTION:str(exc)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def home(request):
    return render(request, 'home.html')

def filter_queryset(self,request,queryset):
        query=dict()
        self.path=re.sub("page\s*[^\n\s]*|&page\s*[^\n\s]*","",self.request.META.get("QUERY_STRING"))
        for key,value in request.GET.items():
            if key in self.filter and value!=None and value.strip()!=str():
                value=[x for x in value.split(",") if x.strip()!=str()]
                if len(value)>1:
                    query[key+"__in"]=value
                elif len(value)!=0:
                    query[key]=value[0]
        if "po_number" in self.request.GET.keys():
            po_number=self.request.GET.get("po_number")
            queryset=queryset.filter(Q(invoice_no__icontains=po_number)|Q(document_po_number__icontains=po_number)|Q(po_number__icontains=po_number)|Q(invoice_id__icontains=po_number))
        return queryset.filter(**query).order_by('-invoice_id')



def GRN(request,*args,**kwrgs):
    invoice_obj=Invoice.objects.get(invoice_id=request.GET.get("invoice_id"))
    coas=CertificateOfAnalysis.objects.filter(invoice_no=invoice_obj.invoice_no,po_number=invoice_obj.po_number)
    return render(request,"GRN.html",{"invoice":invoice_obj,"coas":coas})
        

def sample(request):
    return render(request, 'sample.html')