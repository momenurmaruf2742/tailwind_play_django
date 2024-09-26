from django.db import models
from hero_section.models import AutoCreateUpdate
# Create your models here.
class FaqSection(AutoCreateUpdate,models.Model):
    title = models.CharField(null=True,blank=True,max_length=255)
    heading = models.CharField(null=True,blank=True,max_length=255)
    description = models.TextField(null=True,blank=True)
    
    def __str__(self):
        return str(self.title)
    
    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'
        
class FaqQuestion(AutoCreateUpdate,models.Model):
    question = models.CharField(null=True,blank=True,max_length=255)
    answer = models.TextField(null=True,blank=True,max_length=255)
    
    def __str__(self):
        return str(self.question)
    
    class Meta:
        verbose_name = 'Faq Question'
        verbose_name_plural = 'Faq Questions'
        
class TeamSection(AutoCreateUpdate,models.Model):
    title = models.CharField(null=True,blank=True,max_length=255)
    heading = models.CharField(null=True,blank=True,max_length=255)
    description = models.TextField(null=True,blank=True)
    
    def __str__(self):
        return str(self.title)
    
    class Meta:
        verbose_name = 'Team Section'
        verbose_name_plural = 'Team Sections'
        
class TeamMember(AutoCreateUpdate,models.Model):
    name = models.CharField(null=True,blank=True,max_length=255)
    designation = models.CharField(null=True,blank=True,max_length=255)
    image = models.ImageField(null=True,blank=True,upload_to='team/image')
    
    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name = 'Team Member'
        verbose_name_plural = 'Team Members'
        
class TeamMemberSocialLink(AutoCreateUpdate,models.Model):
    team = models.ForeignKey(TeamMember,on_delete=models.CASCADE)
    name = models.CharField(null=True,blank=True,max_length=50)
    svg_image = models.TextField(null=True,blank=True)
    link = models.TextField(null=True,blank=True)
    
    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name = 'Social'
        verbose_name_plural = 'Socials'