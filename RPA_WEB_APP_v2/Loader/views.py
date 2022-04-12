from django.core import paginator
from django.db.models import manager
from django.http import request
from django.shortcuts import render
from django.views import View
from RestApp.models import *
from RestApp.serializers import *
from utils import Properties
from django.conf import settings
from django.db.models import Q
from django.core.paginator import Paginator
import re
# Create your views here.
class  LoadInvoiceData(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.filter=["status"]
    def get_page_number(self,request,page_obj):
        try:
            self.page_no=int(request.GET.get("page"))
            if self.page_no>page_obj.num_pages:
                self.page_no=1
        except Exception as exc:
            self.page_no=1
    
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
            
    def get(self,request,*args,**kwrgs):
        index=3
        objs=Invoice.objects.all()
        page_obj=Paginator(self.filter_queryset(request,objs),10)
        self.get_page_number(request,page_obj)
        page=page_obj.page(self.page_no)
        if page_obj.num_pages<self.page_no+index:
            page_range=range(self.page_no,page_obj.num_pages)
        else:
            page_range=range(self.page_no,self.page_no+index)
        return render(request,"index.html",{"data":page.object_list,"page_range":page_range,"page":page,"paginator":page_obj,"hider":"invisible","IP_ADDRESS":settings.IP_ADDRESS,"path":self.path})
        