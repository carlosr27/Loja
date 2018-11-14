from django.http import Http404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render


def home(request):
    
    context = {}

    return render(request, '', context)


def products(request):
    context = {}

    return render(request, '', context)


def detail(request):
    context = {}

    return render(request, '', context)



