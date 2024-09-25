from django.contrib import admin
from .models import Pricing,PricingPlan,PricingFeature
# Register your models here.

class FeatureInline(admin.TabularInline):
    model = PricingFeature
    fk_name = 'pricing_plans'
    extra = 1
    

@admin.register(Pricing)
class PricingAdmin(admin.ModelAdmin):
    list_display = ['title',]
    

@admin.register(PricingPlan)
class PricingPlanAdmin(admin.ModelAdmin):
    list_display = ['name','price',]
    inlines = [FeatureInline]