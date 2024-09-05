from django.db import models

# Create your models here.
class HeroContant(models.Model):
    title = models.models.CharField(null= True,blank=True,max_length=255)
    description = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now=())
    
    
    