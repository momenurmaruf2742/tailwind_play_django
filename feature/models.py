from django.db import models
from hero_section .models import AutoCreateUpdate
# Create your models here.
class Feature(AutoCreateUpdate,models.Model):
    name = models.CharField(null=True,blank=True,max_length=255,help_text="Name of service like: Feature")
    title = models.CharField(null=True,blank=True,max_length=255)
    description = models.TextField(null=True,blank=True)
    
    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name = 'Feature'
        verbose_name_plural = 'Features'

class FeatureItem(AutoCreateUpdate,models.Model):
    features = models.ForeignKey(Feature,on_delete=models.CASCADE)
    name = models.CharField(max_length=255,null=True,blank=True)
    title = models.CharField(max_length=255,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    link = models.TextField(null=True,blank=True)
    link_title = models.CharField(max_length=255,null=True,blank=True)
    svg_image = models.TextField(null=True,blank=True)

    def __str__(self):
        return str(self.title)
    
    class Meta:
        verbose_name = 'Feature item'
        verbose_name_plural = 'Feature items'
