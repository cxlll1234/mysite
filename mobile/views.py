#coding=utf-8
from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse
from mobile import models
# Create your views here.
def index(request):
    template = get_template('mobile/index.html')
    products = models.Product.objects.all()
    html = template.render(locals())
    return HttpResponse(html)