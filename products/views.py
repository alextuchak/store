from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.core.cache import cache

from common.views import TitleMixin
from products.models import Basket, ProductCategory, Products, ProductsGallery


class IndexView(TitleMixin, TemplateView):
    template_name = 'products/index.html'
    title = 'Store'


class ProductsListView(TitleMixin, ListView):
    model = Products
    template_name = 'products/products.html'
    paginate_by = 6
    title = 'Store - каталог'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsListView, self).get_context_data()
        context['categories'] = ProductCategory.objects.all()
        return context

    def get_queryset(self):
        queryset = super(ProductsListView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id) if category_id else queryset


class ProductView(ListView):
    model = Products
    template_name = 'products/product.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductView, self).get_context_data()
        context['gallery'] = ProductsGallery.objects.filter(product=self.kwargs['product_id'])
        context['product'] = context['object_list'].get(id=self.kwargs['product_id'])
        return context


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
    cashed_basket = cache.get(request.user.username + '_baskets')
    if cashed_basket:
        cache.delete(request.user.username + '_baskets')
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    cashed_basket = cache.get(request.user.username + '_baskets')
    if cashed_basket:
        cache.delete(request.user.username + '_baskets')
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
