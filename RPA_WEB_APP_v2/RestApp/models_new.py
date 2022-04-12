from pyexpat import model
from tkinter import CASCADE
from django.db import models


class DocumentTypes(models.Model):
    document_type_id=models.BigAutoField(primary_key=True)
    document_name=models.CharField(max_length=150,blank=True,null=True)
    created_on=models.DateTimeField(auto_now=True)
    edited_on=models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return self.document_name

class DocumentIdentifier(models.Model):
    documnet_identifier_id=models.BigAutoField(primary_key=True)
    identifier_keyword=models.CharField(max_length=500,blank=True,null=True)
    document_type=models.ForeignKey(DocumentTypes,on_delete=models.CASCADE,blank=True,null=True)
    created_on=models.DateTimeField(auto_now=True)
    edited_on=models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return f"{self.identifier_keyword},{self.document_type}"

class DocumentFields(models.Model):
    CHOICES=(
        ("SINGLE","SINGLE"),
        ("MULTIPLE","MULTIPLE")
    )
    document_field_id=models.BigAutoField(primary_key=True)
    field_name=models.CharField(max_length=200,blank=True,null=True)
    field_type=models.CharField(max_length=100,blank=True,null=True,choices=CHOICES)
    document_type=models.ForeignKey(DocumentTypes,on_delete=models.CASCADE,blank=True,null=True)
    date_field=models.BooleanField(default=False)
    created_on=models.DateTimeField(auto_now=True)
    edited_on=models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return f"{self.field_name},{self.field_type},{self.document_type}"

class FieldIdentifiers(models.Model):
    field_identifier_id=models.BigAutoField(primary_key=True)
    field_keyword=models.CharField(max_length=200,blank=True,null=True)
    document_field=models.ForeignKey(DocumentFields,on_delete=models.CASCADE,blank=True,null=True)
    document_type=models.ForeignKey(DocumentTypes,on_delete=models.CASCADE,blank=True,null=True)
    created_on=models.DateTimeField(auto_now=True)
    edited_on=models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return f"{self.field_keyword},{self.document_field},{self.document_type}"

class RegexTemplates(models.Model):
    regex_template_id=models.BigAutoField(primary_key=True)
    template=models.CharField(max_length=1000,blank=True,null=True)
    document_field=models.ForeignKey(DocumentFields,on_delete=models.CASCADE,blank=True,null=True)
    document_type=models.ForeignKey(DocumentTypes,on_delete=models.CASCADE,blank=True,null=True)
    reated_on=models.DateTimeField(auto_now=True)
    edited_on=models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return f"{self.template},{self.document_field},{self.document_type}"

class DateFormatRegexTemplate(models.Model):
    date_format_regex_template_id=models.BigAutoField(primary_key=True)
    template=models.CharField(max_length=1000,blank=True,null=True)
    reated_on=models.DateTimeField(auto_now=True)
    edited_on=models.DateTimeField(blank=True,null=True)
