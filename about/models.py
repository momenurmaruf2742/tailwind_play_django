from django.db import models
from django_quill.fields import QuillField
from hero_section.models import AutoCreateUpdate

# Create your models here.
# About page model
class About(AutoCreateUpdate,models.Model):
    title = models.CharField(null=True,blank=True,max_length=250)
    content = QuillField(null=True,blank=True)
    
    def __str__(self):
        return str(self.title)
    
    class Meta:
        verbose_name = "About"    
        verbose_name_plural = "Abouts"    
class AboutImage(AutoCreateUpdate,models.Model):
    abouts = models.ForeignKey(About, on_delete=models.CASCADE)
    name = models.CharField(null=True,blank=True, max_length=50)
    image = models.ImageField(upload_to='about/image')
    
    def __str__(self):
        return str(self.name)
    class Meta:
        verbose_name = "About Image"    
        verbose_name_plural = "About Images" 
    
    
class AboutButton(AutoCreateUpdate,models.Model):
    abouts = models.ForeignKey(About,on_delete=models.CASCADE)
    button_name = models.CharField(null=True,blank=True, max_length=50)
    button_link = models.TextField(null=True,blank=True)
    
    def __str__(self):
        return str(self.button_name)
    class Meta:
        verbose_name = "About Button"
        verbose_name_plural = "About Buttons"

class Experience(AutoCreateUpdate,models.Model):
    abouts = models.ForeignKey(About,on_delete=models.CASCADE)
    title = models.CharField(null=True,blank=True,max_length=255)
    description = models.CharField(null=True,blank=True,max_length=255)
    years = models.IntegerField(default=0)
    
    def __str__(self):
        return str(self.years)
    
    class Meta:
        verbose_name = "Experience"
        verbose_name_plural = "Experiences"
    
    