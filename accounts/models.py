from django.contrib.auth.models import AbstractUser
from accounts.usermanager import CustomUserManager
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    
    class Roles(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        STUDENT = "STUDENT", "Student"
        TEACHER = "TEACHER", "Teacher"
        
    username = None      
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)  
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=20, choices=Roles.choices, default=Roles.STUDENT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    
    def __str__(self):
        return f"{self.email} - {self.id}"