from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('adportal/', admin.site.urls),

    path('', include('product.urls')),
]
