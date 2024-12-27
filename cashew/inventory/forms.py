from django import forms
from .models import *
class Product_Form(forms.ModelForm):
    class Meta:
        model=product
        fields='__all__'
        widgets={
            "product_name":forms.TextInput(attrs={"class":"form-control"}),
            "product_variety":forms.TextInput(attrs={"class":"form-control"}),
            "gst":forms.NumberInput(attrs={"class":"form-control"}),
            "amount":forms.NumberInput(attrs={"class":"form-control"}),
            "picture":forms.FileInput(attrs={"class":"form-control"})
            
            
        }