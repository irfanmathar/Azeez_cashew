from django.shortcuts import render,redirect
from authentication.models import *
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
@login_required(login_url='/')
def home(request):
    if request.user.is_authenticated:
        username=request.user.username
    else:
        username=None
    
    
    return render(request,'home.html',{'username':username})
def addproduct(request):
    context={
        "product_form":Product_Form()
    }
    if request.method=='POST':
        product_form=Product_Form(request.POST,request.FILES)
        if product_form.is_valid():
            product_form.save()
            return redirect('/inventory/allproduct/')
    return render(request,'product.html',context)

def allproduct(request):
    context={
        "all_product":product.objects.all()
    }
    return render(request,'allproduct.html',context)
def deleteproduct(request,id):
    selected_product=product.objects.get(id=id)
    selected_product.delete()
    return redirect('/inventory/allproduct/')
def updateproduct(request,id):
    selected_product=product.objects.get(id=id)
    context={
        "product_form":Product_Form(instance=selected_product)
    }
    if request.method=='POST':
        product_form=Product_Form(request.POST,request.FILES,instance=selected_product)
        if product_form.is_valid():
            product_form.save()
            return redirect("/inventory/allproduct/")
    return render(request,'product.html',context)
        
    
    
