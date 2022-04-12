from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models_new import *
# Create your models here.
class Invoice(models.Model):
    invoice_id=models.AutoField(primary_key=True,db_column="INVOICE_ID")
    status=models.CharField(max_length=500,db_column="STATUS",blank=True,null=True)
    bot_comments=models.CharField(max_length=500,db_column="BOT COMMENTS",blank=True,null=True)
    sender_name=models.CharField(max_length=500,db_column="SENDER_NAME",blank=True,null=True)
    sender_email=models.CharField(max_length=500,db_column="SENDER_EMAIL",blank=True,null=True)
    po_number=models.CharField(max_length=500,db_column="PO_NUMBER",blank=True,null=True)
    document_po_number=models.CharField(max_length=500,db_column="DOCUMENT_PO_NUMBER",blank=True,null=True)
    invoice_no=models.CharField(max_length=500,db_column="INVOICE_NO",blank=True,null=True)
    invoice_date=models.CharField(max_length=500,db_column="INVOICE_DATE",blank=True,null=True)
    po_number=models.CharField(max_length=500,db_column="PO_NUMBER",blank=True,null=True)
    description=models.CharField(max_length=500,db_column="DESCRIPTION",blank=True,null=True)
    bill_of_entry_no=models.CharField(max_length=500,db_column="BILL_OF_ENTRY_NO",blank=True,null=True)
    grn=models.CharField(max_length=500,db_column="GRN",blank=True,null=True)
    invoice_path=models.TextField(db_column="INVOICE_PATH",blank=True,null=True)
    boe_doc_path=models.TextField(db_column="BOE_DOC_PATH",blank=True,null=True)
    bill_of_ladding=models.TextField(db_column="BILL_OFF_LADDING",blank=True,null=True)
    created_on=models.DateTimeField(auto_now=True,blank=True,null=True)
    created_by=models.IntegerField(blank=True,null=True)
    edited_on=models.DateTimeField(blank=True,null=True)
    edited_by=models.IntegerField(blank=True,null=True)
    class Meta:
        db_table="INVOICE"
class CertificateOfAnalysis(models.Model):
    certificate_of_analsys_id=models.AutoField(primary_key=True,db_column="CERTIFICATE_OF_ANALSYS_ID")
    invoice_no=models.CharField(max_length=500,db_column="INVOICE_NO",blank=True,null=True)
    po_number=models.CharField(max_length=500,db_column="PO_NUMBER",blank=True,null=True)
    batch=models.CharField(max_length=500,db_column="BATCH",blank=True,null=True)
    quantity=models.CharField(max_length=500,db_column="QUANTITY",blank=True,null=True)
    date_of_manfacture=models.CharField(max_length=500,db_column="DATE_OF_MANFACTURE",blank=True,null=True)
    unit=models.CharField(max_length=500,db_column="UNIT",blank=True,null=True)
    coa_text=models.CharField(max_length=500,db_column="COA_TEXT",blank=True,null=True)
    expiry_date=models.CharField(max_length=255,db_column="EXPIRY_DATE",blank=True,null=True)
    doc_path=models.CharField(max_length=500,db_column="DOC_PATH",blank=True,null=True)
    created_on=models.DateTimeField(auto_now=True,blank=True,null=True)
    deleted_status=models.BooleanField(blank=True,null=True,default=False)
    created_by=models.IntegerField(blank=True,null=True)
    edited_on=models.DateTimeField(blank=True,null=True)
    edited_by=models.IntegerField(blank=True,null=True)
    class Meta:
        db_table="COA"

class InvoiceTableData(models.Model):
    invoice_table_data_id=models.BigAutoField(primary_key=True)
    invoice=models.ForeignKey(Invoice,on_delete=models.CASCADE,blank=True,null=True)
    material_name=models.TextField(db_column="MATERIAL_NAME",blank=True,null=True)
    quantity=models.CharField(max_length=500,db_column="QUANTITY",blank=True,null=True)
    unit=models.CharField(max_length=500,db_column="UNIT",blank=True,null=True)
    hsn=models.CharField(max_length=500,db_column="HSN",blank=True,null=True)
    amount=models.CharField(max_length=500,db_column="AMOUNT",blank=True,null=True)
    batch_no=models.CharField(max_length=500,db_column="BATCH_NO",blank=True,null=True)
    created_on=models.DateTimeField(auto_now=True,blank=True,null=True)
    edited_on=models.DateTimeField(blank=True,null=True)

@receiver(post_delete,sender=Invoice,dispatch_uid="x")
def deleted_coa(sender, instance, using, **kwargs):
    CertificateOfAnalysis.objects.filter(invoice_no=instance.invoice_no,po_number=instance.po_number).delete()
