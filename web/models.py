from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

class ProjectsModel(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='projects/images/%Y/%m/%d/')
    short_description = models.TextField()
    posted_on = models.DateTimeField(auto_now_add=True)
    link = models.URLField()

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        ordering = ('-id',)

    def __str__(self):
        return self.title

class ContactModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    description = models.TextField()
    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
        ordering = ('-id',)

    def __str__(self):
        return self.first_name
