from django.contrib import admin
from . models import *
# Register your models here.


class HeroButtonInline(admin.TabularInline):
    model = HeroButton
    extra = 1
    fk_name = "hero_contant"
    # readonly_fields = ('hero_contant', 'title', 'svg')
  

@admin.register(HeroContant)
class HeroContantAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [HeroButtonInline]
    
    
