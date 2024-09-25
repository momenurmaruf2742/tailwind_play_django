from django.contrib import admin

# Register your models here.
from .models import Testimonial,TestimonialSection

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'company_name', 'star_rating', 'created_at')
    search_fields = ('client_name', 'company_name')
    

@admin.register(TestimonialSection)
class TestimonialSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'created_at')
    search_fields = ('title', 'subtitle')