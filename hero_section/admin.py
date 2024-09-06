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
    
    
class TechnologySvgInline(admin.TabularInline):
    model = TechnologySvg
    extra = 1
    fk_name = "contant"

@admin.register(TechnologyUses)
class TechnologyUsesAdmin(admin.ModelAdmin):
    list_display = ('contant',)
    inlines = [TechnologySvgInline]
    