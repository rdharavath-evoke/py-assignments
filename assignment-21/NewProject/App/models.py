from django.db import models

#Create your models here
class Xref(models.Model):
    sid=models.CharField(max_length=6)
    Vendor=models.CharField(max_length=200)
    Base_Code=models.CharField(max_length=200)
    COA_Charecteristic=models.CharField(max_length=200)
    COA_UNIT=models.CharField(max_length=200)
    COA_Specification=models.CharField(max_length=200)
    SAP_Group=models.CharField(max_length=200)
    SAP_Group_Counter=models.CharField(max_length=200)
    SAP_Charecteristic=models.CharField(max_length=200)
    SAP_accepted_result=models.CharField(max_length=200)
    SAP_rejected_result=models.CharField(max_length=200)
    Material=models.CharField(max_length=200)
    Material_Description=models.CharField(max_length=200)
    Change_Log=models.CharField(max_length=200)
    Version=models.CharField(max_length=200)
    

    
    
    def __str__(self):
        return self.sid
    objects = models.Manager()