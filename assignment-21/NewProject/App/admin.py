from django.contrib import admin
from .models import Xref
from import_export.admin import ImportExportModelAdmin

# Register your models here.
admin.site.register(Xref)
class XrefAdmin(ImportExportModelAdmin):
    list_display = ('sid','Vendor','Base_Code','COA_Charecteristic','COA_UNIT','COA_Specification','SAP_Group','SAP_Group_Counter','SAP_Charecteristic','SAP_accepted_result','SAP_rejected_result','Material','Material_Description','Change_Log','Version')