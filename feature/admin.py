from django.contrib import admin
from.models import Feature,FeatureItem
# Register your models here.
class FeatureItemInline(admin.TabularInline):
    model = FeatureItem
    extra = 1
    fk_name = "features"
    
@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('name','title',)
    inlines = [FeatureItemInline]    
