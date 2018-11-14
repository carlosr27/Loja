from django.db import models
from django.utils.translation import gettext as _

# from loja.utils import rename_image


class Image(models.Model):
    image = models.ImageField(_('Image'), upload_to='product')
    small = models.ImageField(_('Small'), upload_to='product', null=True, blank=True)

    class Meta:
        verbose_name = _('Image')
        verbose_name_plural = _('Images')
