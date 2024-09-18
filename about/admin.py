from django.contrib import admin
from .models import About,AboutButton,AboutImage,Experience
# Register your models here.

class AboutButtonInline(admin.TabularInline):
    model=AboutButton
    fk_name = 'abouts'
    extra = 1
    

class AboutImageInline(admin.TabularInline):
    model=AboutImage
    fk_name = 'abouts'
    extra = 1
class ExperienceInline(admin.TabularInline):
    model = Experience
    fk_name = 'abouts'
    extra = 1

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [AboutImageInline,AboutButtonInline,ExperienceInline]