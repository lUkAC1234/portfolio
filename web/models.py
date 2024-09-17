from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator
import locale
from django.utils import translation

class UserModel(AbstractUser):
    pass

class ExperienceModel(models.Model):
    logo = models.FileField(
        upload_to='experience/logo/%Y/%m/%d/', 
        verbose_name=_('Лого'),
        validators=[FileExtensionValidator(allowed_extensions=['svg', 'jpeg', 'jpg', 'webp', 'png'])]
    )
    company = models.CharField(max_length=100, verbose_name=_('Компания'))
    text = models.TextField(verbose_name=_('Описание'))
    start_date = models.DateField(verbose_name=_('Дата начала'), null=True, blank=True)  
    end_date = models.DateField(verbose_name=_('Дата окончания'), null=True, blank=True)  

    class Meta:
        verbose_name = _('Опыт в компаниях')
        verbose_name_plural = _('Опыт в компаниях')
        ordering = ('-id',)

    def __str__(self):
        return self.company
    
    def get_work_period(self):
        with translation.override('ru'):
            start = self.start_date.strftime('%b %Y')
            if self.end_date:
                end = self.end_date.strftime('%b %Y')
            else:
                end = _('Настоящее время')
            months_translation = {
                'Jan': 'Янв', 'Feb': 'Фев', 'Mar': 'Мар', 'Apr': 'Апр', 'May': 'Май', 'Jun': 'Июн',
                'Jul': 'Июл', 'Aug': 'Авг', 'Sep': 'Сен', 'Oct': 'Окт', 'Nov': 'Ноя', 'Dec': 'Дек'
            }
            start = months_translation.get(start[:3], start[:3]) + start[3:]
            if end != _('Настоящее время'):
                end = months_translation.get(end[:3], end[:3]) + end[3:]
            return f"{start} - {end}"

class ProjectsModel(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('Название проекта'))
    image = models.ImageField(upload_to='projects/images/%Y/%m/%d/', verbose_name=_('Изображение'))
    short_description = models.TextField(verbose_name=_('Краткое описание'))
    posted_on = models.DateTimeField(auto_now_add=True, verbose_name=_('Дата публикации'))
    link = models.URLField(verbose_name=_('Ссылка'))

    class Meta:
        verbose_name = _('Проект')
        verbose_name_plural = _('Проекты')
        ordering = ('-id',)

    def __str__(self):
        return self.title

class ContactModel(models.Model):
    first_name = models.CharField(max_length=100, verbose_name=_('Имя'))
    last_name = models.CharField(max_length=100, verbose_name=_('Фамилия'))
    description = models.TextField(verbose_name=_('Описание'))

    class Meta:
        verbose_name = _('Контакт')
        verbose_name_plural = _('Контакты')
        ordering = ('-id',)

    def __str__(self):
        return self.first_name