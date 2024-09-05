from django.db import models
from svgImage import SVGAndImageFormField
# Create your models here.

class AutoCreateUpdate(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
     
class HeroContant(AutoCreateUpdate, models.Model):
    title = models.CharField(null= True,blank=True,max_length=255)
    description = models.TextField(null=True,blank=True)
    
class HeroButton(AutoCreateUpdate, models.Model):
    # hero_contant = models.ForeignKey(HeroContant,on_delete=models.CASCADE)
    title = models.CharField(null=True,blank=True,max_length=255)
    button_svg = models.TextField()