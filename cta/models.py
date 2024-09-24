from django.db import models
from hero_section.models import AutoCreateUpdate

# Create your models here.
class Cta(AutoCreateUpdate,models.Model):
    cta_title = models.CharField(null=True,blank=True,max_length=250)
    cta_subtitle = models.CharField(null=True,blank=True, max_length=250)
    cta_description = models.TextField(null=True,blank=True)
    
    
    def __str__(self):
        return str(self.cta_title)
    class Meta:
        verbose_name = "CTA"
        verbose_name_plural = "CTAs"

class CtaButton(AutoCreateUpdate,models.Model):
    ctas= models.ForeignKey(Cta,on_delete=models.CASCADE)
    button_name = models.CharField(null=True,blank=True,max_length=255)
    button_link = models.TextField(null=True,blank=True)
    
    def __str__(self):
        return str(self.button_name)
    
    class Meta:
        verbose_name = 'CTA Button'
        verbose_name_plural = 'CTA Buttons'
    
    