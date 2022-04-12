from rest_framework import serializers
from .models import *
from django.db.models import Q

class CertificateOfAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model=CertificateOfAnalysis
        fields="__all__"
class InvoiceSerializer(serializers.ModelSerializer):
    # coas=serializers.SerializerMethodField()
    coas_count=serializers.SerializerMethodField()
    class Meta:
        model = Invoice
        fields = "__all__"
    # def get_coas(self,instance):
        # return [dict(x) for x in CertificateOfAnalysisSerializer(CertificateOfAnalysis.objects.filter(invoice_no=instance.invoice_no),many=True).data]
    def get_coas_count(self,instance):
        return CertificateOfAnalysis.objects.filter(Q(deleted_status=False)|Q(deleted_status=None),invoice_no=instance.invoice_no,po_number=instance.po_number).count()
class InvoiceSerializerandCoa(serializers.ModelSerializer):
    coas=serializers.SerializerMethodField()
    class Meta:
        model = Invoice
        fields = "__all__"
    def get_coas(self,instance):
        return [dict(x) for x in CertificateOfAnalysisSerializer(CertificateOfAnalysis.objects.filter(Q(deleted_status=False)|Q(deleted_status=None),invoice_no=instance.invoice_no,po_number=instance.po_number),many=True).data]
    
