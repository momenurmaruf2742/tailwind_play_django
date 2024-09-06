from django.db import models
from svgImage import SVGAndImageFormField
# Create your models here.

class AutoCreateUpdate(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
     
class HeroContant(AutoCreateUpdate, models.Model):
    title = models.CharField(null= True,blank=True,max_length=255)
    description = models.TextField(null=True,blank=True)

    image = models.ImageField(upload_to='hero_section/images',help_text="Image must be 845(W) × 329(H) px" ,default="")
    
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
    DESIGN_CHOICES = [
        ('primary', 'Primary'),
        ('secondary', 'Secondary'),
    ]
    design_type = models.CharField(max_length=10, choices=DESIGN_CHOICES, default='primary')

    
    def __str__(self):
        return str(self.title)
    class Meta:
        verbose_name = 'Hero Button'
        verbose_name_plural = 'Hero Buttons'

class TechnologyUses(AutoCreateUpdate,models.Model):
    contant = models.CharField(null=True,blank=True,max_length=255)
    description = models.TextField(null=True,blank=True)

    def __str__(self):
        return str(self.contant)
    class Meta:
        verbose_name = 'Technology contant'
        verbose_name_plural = 'Technology contants'

class TechnologySvg(AutoCreateUpdate,models.Model):
    contant = models.ForeignKey(TechnologyUses,on_delete=models.CASCADE)
    name = models.CharField(null=True,blank=True,max_length=255)
    link = models.TextField(null=True,blank=True)
    svg_image = models.TextField(null=True,blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Technology SVG'
        verbose_name_plural = 'Technology SVGs'    
