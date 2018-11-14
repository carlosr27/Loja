from ckeditor.fields import RichTextField

from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext as _

from image.models import Image


class BannerTop(models.Model):
    group_position = models.PositiveSmallIntegerField(
        _('Group Position'), validators=[MinValueValidator(1)], default=1
    )
    active = models.BooleanField(_('Active'), default=True)
    date = models.DateTimeField(_('Date'), auto_now_add=True)

    class Meta:
        ordering = 'group_position',
        verbose_name = _('Banner Top')
        verbose_name_plural = _('Banners Top')


class BannerTopImage(models.Model):
    banner = models.ForeignKey(BannerTop, verbose_name=_('Banner'), on_delete=models.CASCADE)
    image = models.ForeignKey(Image, verbose_name=_('Image'), on_delete=models.CASCADE)
    position = models.PositiveSmallIntegerField(
        _('Position'), validators=[MinValueValidator(1)], default=1
    )
    link = models.URLField(_('Link'), null=True, blank=True)


class BannerBottom(models.Model):
    image = models.ForeignKey(Image, verbose_name=_('Image'), on_delete=models.CASCADE)
    position = models.PositiveSmallIntegerField(
        _('Position'), validators=[MinValueValidator(1)], default=1
    )
    link = models.URLField(_('Link'), null=True, blank=True)
    active = models.BooleanField(_('Active'), default=True)
    date = models.DateTimeField(_('Date'), auto_now_add=True)

    class Meta:
        ordering = 'position',
        verbose_name = _('Banner Bottom')
        verbose_name_plural = _('Banners Bottom')
