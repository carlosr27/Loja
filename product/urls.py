from django.urls import path
from django.utils.translation import gettext_lazy as _

from product.views import home, products, detail


urlpatterns = [
    path('', home, name='home'),
    path('{}/'.format(_('products')), products, name='products'),
    path('{}/<slug:product_slug/'.format(_('products')), detail, name='detail'),
]
