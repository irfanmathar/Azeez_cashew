from django.db import models
from django.utils.html import format_html


class product(models.Model):
    product_name=models.CharField(max_length=200,null=True)
    
    product_variety=models.CharField(max_length=200,null=True)
    gst=models.FloatField(default=0)
    amount=models.FloatField(default=0)
    picture=models.ImageField(null=True,upload_to='images/')
    
    def __str__(self):
        return self.product_name+"--Rs."+str(self.amount)

    

    

    
    
