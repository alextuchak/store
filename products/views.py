from django.shortcuts import render
from products.models import ProductCategory, Products
# Create your views here.


def index(request):
    return render(request, 'products/index.html')


def products(request):
    context ={
        'title': 'Store',
        'products': Products.objects.all(),
        'categories': ProductCategory.objects.all()
    }
    return render(request, 'products/products.html', context)