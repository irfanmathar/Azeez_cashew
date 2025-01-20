from django.db import models
from inventory.models import *
from authentication.models import *




class Order(models.Model):
    
    date = models.DateTimeField(auto_now_add=True)
    product_reference=models.ForeignKey(product,on_delete=models.SET_NULL,null=True)
    phone_number=models.CharField(max_length=10,null=True)
    shop_name=models.CharField(max_length=100,null=True)
    address=models.CharField(max_length=100,null=True)
    landmark=models.CharField(max_length=100,null=True)
    prefer_date=models.DateField(null=True)
    quantity=models.FloatField(default=0)
    amount=models.FloatField(default=0)
    gst_amount=models.FloatField(default=0)
    bill_amount=models.FloatField(default=0)
    
    
    
    