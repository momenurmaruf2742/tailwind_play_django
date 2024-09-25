from django.db import models
from hero_section.models import AutoCreateUpdate
# Create your models here.

class Testimonial(AutoCreateUpdate,models.Model):
    client_name = models.CharField(max_length=255)
    client_position = models.CharField(max_length=255, help_text="e.g., Founder @ Rolex")
    feedback = models.TextField()
    star_rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=5)
    author_image = models.ImageField(upload_to='testimonials/')
    company_name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.client_name} ({self.company_name})'

    # class Meta:
    #     ordering = ['-created_at']
        
class TestimonialSection(AutoCreateUpdate,models.Model):
    title = models.CharField(max_length=255, default="What our Clients Say")
    subtitle = models.CharField(max_length=255, default="Testimonials")
    description = models.TextField(default="There are many variations of passages of Lorem Ipsum available but the majority have suffered alteration in some form.")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Testimonial Section"
        verbose_name_plural = "Testimonial Sections"