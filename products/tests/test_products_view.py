from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus
from model_bakery import baker
from products.models import Products, ProductCategory


class ProductsListViewTestCase(TestCase):

    def setUp(self) -> None:
        self.products = baker.make(Products, _quantity=6, image='media/products_images/Adidas-hoodie.png')

    def _common_tests(self, response):
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Store - каталог')
        self.assertTemplateUsed(response, 'products/products.html')

    def test_list(self):
        path = reverse('products:index')
        response = self.client.get(path)
        self._common_tests(response)
        self.assertEqual(list(response.context_data['object_list']), self.products[:3])
        self.assertEqual(response.context_data['is_paginated'], True)

    def test_list_with_category(self):
        category = ProductCategory.objects.first()
        path = reverse('products:category', kwargs={"category_id": category.id})
        response = self.client.get(path)
        self._common_tests(response)
        self.assertEqual(list(response.context_data['object_list']),
                         list(Products.objects.filter(category_id=category.id)))

    def test_list_page(self):
        path = reverse('products:paginator', kwargs={"page": 2})
        response = self.client.get(path)
        self._common_tests(response)
        self.assertEqual(list(response.context_data['object_list']), self.products[3:6])