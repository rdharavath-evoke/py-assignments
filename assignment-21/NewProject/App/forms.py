from django import forms
from django.forms import fields
from .models import Xref

class ApplicationForm(forms.ModelForm):
    class Meta:
        model=Xref
        fields='__all__'
        
        
