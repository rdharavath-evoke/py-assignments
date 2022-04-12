from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from .views import *
urlpatterns = [
    # path('index/', lambda request:render(request,"index.html")),
    path('index/', LoadInvoiceData.as_view(),name="Home"),
]
