from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe
from .models import ContactModel, ProjectsModel

@admin.register(ContactModel)
class Contactadmin(admin.ModelAdmin):
    list_display = ['id', 'first_name']
    list_display_links = ['id', 'first_name']
    search_fields = ['first_name']

@admin.register(ProjectsModel)
class Projectsadmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
    search_fields = ['title']


