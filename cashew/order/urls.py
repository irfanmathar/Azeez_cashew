from django.urls import path
from .views import *
urlpatterns=[
    path('addorder/',addorder),
    path('allorder/',allorder)
    
]