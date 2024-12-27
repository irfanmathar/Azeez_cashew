from django.urls import path
from .views import *
urlpatterns=[
    path('home/',home),
    path('product/',addproduct),
    path('allproduct/',allproduct),
    
    path('product/delete/<int:id>/',deleteproduct,name="product_delete"),
    path('product/update/<int:id>/',updateproduct,name="product_update")
]