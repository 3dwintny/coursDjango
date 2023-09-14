from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    
    websote = models.URLField(max_length=200, blank=True)
    bigorapy = models.TextField(blank=True)
    phone_number = models.CharField(max_length=30)
    