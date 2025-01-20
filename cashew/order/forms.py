from django import forms
from .models import *
from .views import *


class Order_Form(forms.ModelForm):
    class Meta:
        model=Order
        fields=['product_reference','phone_number','shop_name','address','landmark','prefer_date','quantity']
        widgets={
            "product_reference":forms.Select(attrs={"class":"form-control"}),
            "phone_number":forms.TextInput(attrs={"class":"form-control"}),
            "shop_name":forms.TextInput(attrs={"class":"form-control"}),
            "address":forms.TextInput(attrs={"class":"form-control"}),
            "landmark":forms.TextInput(attrs={"class":"form-control"}),
            "prefer_date":forms.DateTimeInput(attrs={"class":"form-control"}),
            "quantity":forms.NumberInput(attrs={"class":"form-control"}),
        }