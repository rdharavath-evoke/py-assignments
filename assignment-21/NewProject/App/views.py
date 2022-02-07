from django.shortcuts import render
from .models import Xref
from django.http import HttpResponseRedirect
from .forms import ApplicationForm


from .resources import XrefResource
from django.contrib import messages
from django.http import HttpResponse
from tablib import Dataset

from django.core.files.storage import FileSystemStorage


def add(request):
    form=ApplicationForm(request.POST or None)
    # student=Student.objects.all()
    if form.is_valid():
        form.save()
    return render(request, 'add.html', {'form':form})

def show(request):
    data=Xref.objects.all()
    return render(request, 'show.html', {'data':data})


def update(request, sid):
    xref = Xref.objects.get(sid=sid)
    form= ApplicationForm(request.POST, instance=xref)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    return render(request, 'update.html', {'xref':xref})

def delete(request, sid):
    form=Xref.objects.get(sid=sid)
    form.delete()
    return HttpResponseRedirect('/')


def upload(request):
    context={}
    if request.method=='POST':
        uploaded_file=request.FILES['myfile']
        fs=FileSystemStorage()
        name=fs.save(uploaded_file.name, uploaded_file)
        context['url']=fs.url(name)
    return render(request, 'upload.html', context)

# def upload(request):
#     file=Xref.objects.all()
#     return render(request, 'upload.html', {'xref':file})

# def upload(request):
#     if request.method=='POST':
#         xref_resource=XrefResource()
#         dataset=Dataset()
#         new_xref=request.FILES['myfile']
        
#         # if not new_xref.endswith('xlsx'):
#         #     messages.info(request,'upload.html')
            
#         imported_data=dataset.load(new_xref.read(),format='xlsx')
#         for data in imported_data:
#             value=Xref(data[0],
#                        data[1],
#                        data[2],
#                        data[3],
#                        data[4],
#                        data[5],
#                        data[6],
#                        data[7],
#                        data[8],
#                        data[9],
#                        data[10],
#                        data[11],
#                        data[12],
#                        data[13]
#                        )
#             value.save()
#     return render(request,'upload.html')



# import pandas as pd
# import os
# from django.conf import settings
# from django.core.files.storage import FileSystemStorage
 
# def upload(request):
#     print('s')               
#     try:
#         if request.method == 'POST' and request.FILES['myfile']:
          
#             myfile = request.FILES['myfile']        
#             fs = FileSystemStorage()
#             filename = fs.save(myfile.name, myfile)
#             uploaded_file_url = fs.url(filename)
#             excel_file = uploaded_file_url
#             print(excel_file) 
#             xrefdata = pd.read_csv("."+excel_file,encoding='utf-8')
#             print(type(xrefdata))
#             dbframe = xrefdata
#             for dbframe in dbframe.itertuples():
                 
#                 obj = Xref.objects.create(sid=dbframe.sid,Vendor=dbframe.Vendor, Base_Code=dbframe.Base_Code,
#                                                 COA_Charecteristic=dbframe.COA_Charecteristic, COA_UNIT=dbframe.COA_UNIT, COA_Specification=dbframe.COA_Specification, 
#                                                 SAP_Group=dbframe.SAP_Group, SAP_Group_Counter=dbframe.SAP_Group_Counter, 
#                                                 SAP_Charecteristic=dbframe.SAP_Charecteristic, SAP_accepted_result=dbframe.SAP_accepted_result,
#                                                 SAP_rejected_result=dbframe.SAP_rejected_result,Material=dbframe.Material,Material_Description=dbframe.Material_Description,
#                                                 Change_Log=dbframe.Change_Log,Version=dbframe.Version)
#                 print(type(obj))
#                 obj.save()
 
#             return render(request, 'upload.html', {
#                 'uploaded_file_url': uploaded_file_url
#             })    
#     except Exception as identifier:            
#         print(identifier)
     
#     return render(request, 'upload.html',{})