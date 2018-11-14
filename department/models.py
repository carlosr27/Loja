from django.db import models
from django.utils.translation import gettext as _

from image.models import Image


class Department(models.Model):
    name = models.CharField(_('Name'), max_length=40)
    image = models.ForeignKey(Image, verbose_name=_('Image'), null=True, blank=True, on_delete=models.CASCADE)


class Category(models.Model):
    # TODO - Manutenção
    name = models.CharField(_('Name'), max_length=36)
    slug = models.SlugField(_('Slug'), unique=True)
    department = models.ForeignKey(Department, verbose_name=_('Department'), on_delete=models.CASCADE)
    active = models.BooleanField(_('Active'), default=True)

    class Meta:
        unique_together = ('slug', 'department')
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    # TODO - Manutenção
    name = models.CharField(_('Name'), max_length=36)
    slug = models.SlugField(_('Slug'), unique=True)
    image = models.ForeignKey(Image, verbose_name=_('Image'), null=True, blank=True, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name=_('Categories'), on_delete=models.CASCADE)
    active = models.BooleanField(_('Active'), default=True)
    home = models.BooleanField(_('Show on home'), default=False)

    class Meta:
        verbose_name = _('Sub-Category')
        verbose_name_plural = _('Sub-Categories')

    def __str__(self):
        return self.name


class Collection(models.Model):
    name = models.CharField(_('Name'), max_length=36)
    slug = models.SlugField(_('Slug'), unique=True)
    sub_category = models.ForeignKey(
        SubCategory, verbose_name=_('Sub-Category'), null=True, blank=True, on_delete=models.CASCADE
    )
    active = models.BooleanField(_('Active'), default=True)

    class Meta:
        verbose_name = _('Collection')
        verbose_name_plural = _('Collections')

    def __str__(self):
        return self.name
