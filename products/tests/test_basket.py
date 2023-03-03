from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus
from model_bakery import baker
from products.models import Products, Basket
from users.models import User


class BasketTestCase(TestCase):

    def setUp(self) -> None:
        self.product = baker.make(Products, _quantity=1)
        self.user = baker.make(User, _quantity=1)
        self.basket = baker.make(Basket, user=self.user[0])

    def test_basket_add(self):
        path = reverse('products:basket_add', kwargs={'product_id': self.product[0].id})
        self.client.force_login(self.user[0])
        response = self.client.post(path, HTTP_REFERER=reverse('products:index'))
        basket = Basket.objects.last()
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertIsInstance(basket, Basket)
        self.assertEqual(basket.user, self.user[0])

    def test_basket_delete(self):
        path = reverse('products:basket_remove', kwargs={'basket_id': self.basket.id})
        self.client.force_login(self.user[0])
        response = self.client.post(path, HTTP_REFERER=reverse('products:index'))
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(Basket.objects.count(), 0)



