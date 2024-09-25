from django.db import models
from hero_section.models import AutoCreateUpdate
# Create your models here.

class Pricing(AutoCreateUpdate,models.Model):
    title = models.CharField(null=True,blank=True,max_length=255)
    heading = models.CharField(null=True,blank=True,max_length=255)
    description = models.TextField(null=True,blank=True)
    
    def __str__(self):
        return str(self.title)
    
    class Meta:
        verbose_name = 'Pricing'
        verbose_name_plural = 'Pricings'

class PricingPlan(AutoCreateUpdate,models.Model):
    name = models.CharField(null=True,blank=True,max_length=255)
    price = models.FloatField(default=0.0)
    wise = models.CharField(null=True,blank=True,max_length=255,help_text="Per Month / Per Year")
    criteria = models.CharField(null=True,blank=True,max_length=255,help_text="Features")
    button = models.CharField(blank=True,null=True,max_length=255)
    button_link = models.TextField(null=True,blank=True)
    recomended = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name = 'Pricing Plan'
        verbose_name_plural = 'Pricing Plans'
        
class PricingFeature(AutoCreateUpdate,models.Model):
    pricing_plans = models.ForeignKey(PricingPlan,on_delete=models.CASCADE)
    name = models.CharField(blank=True,null=True,max_length=255)
    
    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name = 'Pricing Feature'
        verbose_name_plural = 'Pricing Features'