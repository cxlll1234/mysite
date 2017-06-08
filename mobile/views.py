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
def detail(request,id):
    try:
        product = models.Product.objects.get(id=id)
        images = models.PPhoto.objects.filter(product=product)
    except:
        pass
    template= get_template('mobile/detail.html')
    html = template.render(locals())
    return HttpResponse(html)