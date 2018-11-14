from django.db import models
from django.utils.translation import gettext as _

from image.models import Image


class Brand(models.Model):
    name = models.CharField(_('Name'), max_length=60, unique=True)
    slug = models.SlugField(_('Slug'), unique=True)
    image = models.ForeignKey(Image, verbose_name=_('Image'), null=True, blank=True, on_delete=models.CASCADE)
    active = models.BooleanField(_('Active'), default=True)
    date = models.DateTimeField(_('Date'), auto_now_add=True)

    class Meta:
        verbose_name = _('Brand')
        verbose_name_plural = _('Brands')
        ordering = '-date',
