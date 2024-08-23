import os
from django.test import TestCase
from rest_framework import status
from lettings import models


class TestCaseLettings(TestCase):

    def setUp(self):
        self.new_address_1_data = {
            'number': 75,
            'street': 'Quai du Louvre',
            'city': 'Paris',
            'state': 'Ile-de-France',
            'zip_code': 75002,
            'country_iso_code': '3166-1',
        }
        self.new_address_1_test = models.Address.objects.create(**self.new_address_1_data)
        self.new_letting_1_data = {
            'title': 'letting_test_1',
            'address': self.new_address_1_test,
        }
        self.new_letting_1_test = models.Letting.objects.create(**self.new_letting_1_data)

    def test_models(self):
        self.new_address_2_data = {
            'number': 76,
            'street': 'Quai du Louvre',
            'city': 'Paris',
            'state': 'Ile-de-France',
            'zip_code': 75002,
            'country_iso_code': '3166-1',
        }
        self.new_address_2_test = models.Address.objects.create(**self.new_address_2_data)
        self.new_letting_2_data = {
            'title': 'letting_test_2',
            'address': self.new_address_2_test,
        }
        self.new_letting_2_test = models.Letting.objects.create(**self.new_letting_2_data)
        self.assertNotEqual(self.new_address_1_test, self.new_address_2_test)
        self.assertNotEqual(self.new_letting_1_test, self.new_letting_2_test)

    def test_views(self):
        self.client.login(username='admin', password=os.getenv('ADMIN_PASSWORD'),)
        self.new_address_1_data['number'] = 74
        response = self.client.post('/admin/lettings/address/add/', self.new_address_1_data,
                                    format='json', follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.new_letting_1_data['title'] = 'letting_test_3'
        response = self.client.post('/admin/lettings/letting/add/', self.new_letting_1_data,
                                    format='json', follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.get('/lettings/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

