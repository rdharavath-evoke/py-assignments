from django.urls import path
from RestApp import views
from.views import LoadAllInvoices,PostCoaRest,SetStatus,LoadInvoice,LoadPdf,DeleteCoa,UpdateInvoice,UpdateCoa,PostCoa,LoadAllCoas
urlpatterns=[
    path("all/invoices/",LoadAllInvoices.as_view(),name="LoadAllInvoices"),
    path("coas/for/invoice/",LoadAllCoas.as_view(),name="LoadAllCoas"),
    path("load/invoice/<int:id>/",LoadInvoice.as_view(),name="LoadInvoice"),
    path("load/pdf/<int:id>/<str:type>/",LoadPdf.as_view(),name="LoadPdf"),
    path("post/coa/rest/",PostCoaRest.as_view(),name="PostCoaRest"),
    path('set/status/',SetStatus.as_view(),name="SetStatus"),
    path("update/invoice/",UpdateInvoice.as_view(),name="UpdateInvoice"),
    path("update/coa/",UpdateCoa.as_view(),name="UpdateCoa"),
    path("post/coa/",PostCoa.as_view(),name="PostCoa"),
    path("delete/coa/",DeleteCoa.as_view(),name="DeleteCoa"),
    path('home/',views.home,name='home'),
    path('get/invoice/',views.GRN,name='GRN'),
    path('sample/',views.sample,name='sample'),
]