from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe
from .models import (
    UserModel,
    ContactModel, 
    ProjectsModel, 
    ExperienceModel
)

@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username']
    list_display_links = ['id', 'username']
    search_fields = ['username']

@admin.register(ContactModel)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name']
    list_display_links = ['id', 'first_name']
    search_fields = ['first_name']

@admin.register(ProjectsModel)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
    search_fields = ['title']

@admin.register(ExperienceModel)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['id', 'company']
    list_display_links = ['id', 'company']
    search_fields = ['company']
    
admin.site.site_header = 'Портфолио'
admin.site.site_title = 'Портфолио'


