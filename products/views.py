from django.shortcuts import render, HttpResponseRedirect
from products.models import ProductCategory, Products, Basket
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


def index(request):
    return render(request, 'products/index.html')


def products(request, category_id=None, page_number=1):
    products = Products.objects.filter(category_id=category_id) if category_id else Products.objects.all()
    paginator = Paginator(products, 3)
    products_paginator = paginator.page(page_number)
    context = {'title': 'Store',
               'categories': ProductCategory.objects.all(),
               'products': products_paginator}
    return render(request, 'products/products.html', context)


@login_required
def basket_add(request, product_id):
    product = Products.objects.get(id=product_id)
    basket = Basket.objects.filter(user=request.user, product=product)

    if not basket.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = basket.first()
        basket.quantity += 1
        basket.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
