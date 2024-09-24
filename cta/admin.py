from django.contrib import admin
from.models import Cta,CtaButton
# Register your models here.
class CtaButtonInline(admin.TabularInline):
    model = CtaButton
    fk_name = 'ctas'
    extra = 1
    
@admin.register(Cta)
class CtaAdmin(admin.ModelAdmin):
    list_display = ['cta_title']
    inlines = [CtaButtonInline]