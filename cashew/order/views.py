from django.shortcuts import render, get_object_or_404
from authentication.models import *
from .models import *
from .forms import *
from django.contrib.auth.decorators import *
from inventory.models import *


def addorder(request):
    context={
        "order_form":Order_Form()
    }
    if request.method=='POST':
        selected_product=product.objects.get(id=request.POST['product_reference'])
        
        amount=selected_product.amount*float(request.POST['quantity'])
        gst_amount=(amount*selected_product.gst)/100
        bill_amount=amount+gst_amount
        new_order=Order(product_reference_id=request.POST['product_reference'],
                        phone_number=request.POST['phone_number'],shop_name=request.POST['shop_name'],address=request.POST['address'],
                        landmark=request.POST['landmark'],
                        prefer_date=request.POST['prefer_date'],quantity=request.POST['quantity'],
                        amount=amount,gst_amount=gst_amount,bill_amount=bill_amount)
        new_order.save()
    return render(request,'addorder.html',context)
def allorder(request):
    context={
        'all_order':Order.objects.all()
    }
    return render(request,'allorder.html',context)
def viewproduct(request):
    context={
        "all_product":product.objects.all()
    }
    return render(request,'addorder.html',context)