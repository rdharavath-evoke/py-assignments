from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Invoice)
admin.site.register(CertificateOfAnalysis)
admin.site.register(DocumentTypes)
admin.site.register(InvoiceTableData)
admin.site.register(DocumentIdentifier)
admin.site.register(DocumentFields)
admin.site.register(FieldIdentifiers)
admin.site.register(RegexTemplates)
admin.site.register(DateFormatRegexTemplate)