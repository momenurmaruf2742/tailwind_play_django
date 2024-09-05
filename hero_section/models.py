from django.db import models
from svgImage import SVGAndImageFormField
# Create your models here.

class AutoCreateUpdate(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
     
class HeroContant(AutoCreateUpdate, models.Model):
    title = models.CharField(null= True,blank=True,max_length=255)
    description = models.TextField(null=True,blank=True)
    
    def __str__(self):
        return str(self.title)
    class Meta:
        verbose_name = 'Hero Contant'
        verbose_name_plural = 'Hero Contants'
        
class HeroButton(AutoCreateUpdate, models.Model):
    hero_contant = models.ForeignKey(HeroContant,on_delete=models.CASCADE)
    title = models.CharField(null=True,blank=True,max_length=255)
    button_link = models.TextField(null=True,blank=True)
    button_svg = models.TextField(null=True,blank=True)
    
    def __str__(self):
        return str(self.title)
    class Meta:
        verbose_name = 'Hero Button'
        verbose_name_plural = 'Hero Buttons'