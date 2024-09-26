from django.contrib import admin
from .models import FaqSection,FaqQuestion,TeamSection,TeamMember,TeamMemberSocialLink
# Register your models here.

class TeamMemberSocialLinkInline(admin.TabularInline):
    model = TeamMemberSocialLink
    fk_name = 'team'
    extra = 1

@admin.register(FaqSection)    
class FaqSectionAdmin(admin.ModelAdmin):
    list_display = ['title','heading',]
    

@admin.register(FaqQuestion)    
class FaqQuestionAdmin(admin.ModelAdmin):
    list_display = ['question',]


@admin.register(TeamSection)    
class TeamSectionAdmin(admin.ModelAdmin):
    list_display = ['title','heading',]


@admin.register(TeamMember)    
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['name',]
    inlines = [TeamMemberSocialLinkInline]