from django.db import models
from django.contrib.auth.models import AbstractUser

class user(AbstractUser):
    age=models.IntegerField(default=0)
    ADMIN=0
    USER=1
    
    role_choices=[
        (ADMIN,'Admin'),
        (USER,'User'),
        
    ]
    role=models.IntegerField(default=0,choices=role_choices)

    
    
    
    
    
