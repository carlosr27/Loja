from ckeditor.fields import RichTextField

from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

from department.models import Category, SubCategory, Collection
# from lojavirtual.utils import rename_image
from image.models import Image


class Color(models.Model):
    # TODO - Color picker
    name = models.CharField(_('Name'), max_length=26, unique=True)
    active = models.BooleanField(_('Active'), default=True)

    class Meta:
        verbose_name = _('Color')
        verbose_name_plural = _('Colors')

    def __str__(self):
        return self.name


class Option(models.Model):
    name = models.CharField(_('Name'), max_length=32)
    active = models.BooleanField(_('Active'), default=True)
    multiple = models.BooleanField(_('Multiple Choices'), default=False)
    select = models.BooleanField(
        _('Values as select?'), default=True,
        help_text='Se o campo multipla escolha for False entao esse campo sera ignorado'
    )

    class Meta:
        verbose_name = _('Option')
        verbose_name_plural = _('Options')

    def __str__(self):
        return self.name


class OptionValue(models.Model):
    name = models.CharField(_('Name'), max_length=32)
    option = models.ForeignKey(Option, verbose_name=_('Option'), on_delete=models.CASCADE)
    text_value = models.CharField(
        _('Textual Value'), max_length=20, help_text='Preencha se essa campo nao for um numero'
    )
    number_value = models.FloatField(
        _('Number Value'), null=True, blank=True,
        help_text='Se o valor textual foi preenchido esse campo sera ignorado'
    )

    class Meta:
        verbose_name = _('Option Value')
        verbose_name_plural = _('Options Values')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(_('Name'), max_length=64)
    slug = models.SlugField(_('Slug'),)
    description = RichTextField(_('Description'))
    category = models.ForeignKey(Category, verbose_name=_('Category'), on_delete=models.CASCADE)
    collection = models.ManyToManyField(Collection, verbose_name=_('Collection')    )
    sub_category = models.ManyToManyField(SubCategory, verbose_name=_('Sub Category'))
    options = models.ManyToManyField(Option, verbose_name=_('Options'))
    # parcel = models.SmallIntegerField(
    #     _('Parcel'), null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(4)],
    #     help_text='Apenas para mostrar na home do site. Limite: até 4x'
    # )
    stock = models.IntegerField(_('Stock'), default=0, help_text='0 = infinito')
    price = models.FloatField(_('Price'))
    old_price = models.FloatField(_('Old Price'), null=True, blank=True)
    promotion = models.FloatField(_('Promotion'), null=True, blank=True, help_text='Substitui o preço')
    active = models.BooleanField(_('Active'), default=True)
    show_home = models.BooleanField(_('Show In Home'), default=True)
    show_promotion = models.BooleanField(
        _('Show Promotion'), default=False, help_text='Mostrar o preço da promoção sobre o preço normal?'
    )
    show_old_price = models.BooleanField(_('Show Old Price'), default=False)
    date = models.DateTimeField(_('Date'), auto_now_add=True)

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.pk:
            current = Product.objects.get(id=self.id)
            if self.price != current.price:
                self.old_price = self.price
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'product_slug': self.slug})


class ProductImage(models.Model):
    product = models.ForeignKey(Product, verbose_name=_('Product'), on_delete=models.CASCADE)
    image = models.ForeignKey(Image, verbose_name=_('Image'), on_delete=models.CASCADE)
    color = models.ForeignKey(Color, verbose_name=_('Color'), null=True, blank=True, on_delete=models.CASCADE)
    position = models.PositiveIntegerField(_('Position'), default=1)

    class Meta:
        verbose_name = _('Product Image')
        verbose_name_plural = _('Product Image')
        unique_together = ('product', 'position')
