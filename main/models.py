from django.db import models
from django.utils.translation import gettext_lazy as _

class Article(models.Model):
    title = models.CharField(max_length=150, blank=False, null=False, verbose_name=_('Наслов'))
    content = models.TextField(blank=False, null=False, verbose_name=_('Содржина'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Креирано на'))

    class Meta:
        ordering = ('-created_at', )
        verbose_name = _('Објава')
        verbose_name_plural = _('Објави')

class ArticleImage(models.Model):
    article = models.ForeignKey(Article, blank=False, null=False, on_delete=models.CASCADE, related_name='images', verbose_name=_('Објава'))
    image = models.ImageField(blank=False, null=False, verbose_name=_('Слика'))
 
    class Meta:
        verbose_name = _('Слика за објава')
        verbose_name_plural = _('Слики за објава')

class Slider(models.Model):
    position = models.CharField(max_length=50, blank=False, null=False, verbose_name=_('Позиција'))
    position_slug = models.SlugField(max_length=50, blank=False, null=False, verbose_name=_('Позиција слаг'))

    class Meta:
        verbose_name = _('Слајдер')
        verbose_name_plural = _('Слајдери')
    
class SliderImage(models.Model):
    slider = models.ForeignKey(Slider, blank=False, null=False, on_delete=models.CASCADE, related_name='images', verbose_name=_('Слајдер'))
    order = models.IntegerField(blank=False, null=False, default=1, verbose_name=_('Редослед'))
    image = models.ImageField(blank=False, null=False, verbose_name=_('Слика'))

    class Meta:
        verbose_name = _('Слика за слајдер')
        verbose_name_plural = _('Слики за слајдер')
    
class GalleryCategory(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False, verbose_name=_('Име'))
    name_slug = models.SlugField(max_length=50, blank=False, null=False, verbose_name=_('Име слаг'))

    class Meta:
        verbose_name = _('Категорија за галерија')
        verbose_name_plural = _('Категории за галерија')

class GalleryImage(models.Model):
    category = models.ForeignKey(GalleryCategory, blank=False, null=False, on_delete=models.RESTRICT, related_name='images', verbose_name=_('Категорија'))
    title = models.CharField(max_length=50, blank=False, null=False, verbose_name=_('Наслов'))
    image = models.ImageField(blank=False, null=False, verbose_name=_('Слика'))

    class Meta:
        verbose_name = _('Слика за галерија')
        verbose_name_plural = _('Слики за галерија')

class Employee(models.Model):
    full_name = models.CharField(max_length=50, blank=False, null=False, verbose_name=_('Вработен'))
    title = models.CharField(max_length=20, blank=False, null=False, verbose_name=_('Титула'))
    email = models.EmailField(blank=False, null=False, verbose_name=_('Емаил'))

    class Meta:
        verbose_name = _('Вработен')
        verbose_name_plural = _('Вработени')
class Subject(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False, verbose_name=_('Име'))
    employees = models.ManyToManyField(Employee, related_name='subjects', verbose_name=_('Вработени'))
 
    class Meta:
        verbose_name = _('Предмет')
        verbose_name_plural = _('Предмети')

class ContactFormMessage(models.Model):
    full_name = models.CharField(max_length=50, blank=False, null=False, verbose_name=_('Име и презиме'))
    email = models.EmailField(blank=False, null=False, verbose_name=_('Емаил'))
    title = models.CharField(max_length=100, blank=False, null=False, verbose_name=_('Наслов'))
    content = models.TextField(blank=True, null=True, verbose_name=_('Содржина'))
    
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('Порака')
        verbose_name_plural = _('Пораки')
