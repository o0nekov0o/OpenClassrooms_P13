import os
from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from profiles import models


class TestCaseProfiles(TestCase):

    def setUp(self):
        self.new_user_1_data = {
            'username': 'user1',
            'password': os.getenv('USER_PASSWORD'),
        }
        self.new_user_1_test = User.objects.create(**self.new_user_1_data)
        self.new_profile_1_data = {
            'user': self.new_user_1_test,
            'favorite_city': 'Paris',
        }
        self.new_profile_1_test = models.Profile.objects.create(**self.new_profile_1_data)

    def test_models(self):
        self.new_user_2_data = {
            'username': 'user2',
            'password': os.getenv('USER_PASSWORD'),
        }
        self.new_user_2_test = User.objects.create(**self.new_user_2_data)
        self.new_profile_2_data = {
            'user': self.new_user_2_test,
            'favorite_city': 'Nanterre',
        }
        self.new_profile_2_test = models.Profile.objects.create(**self.new_profile_2_data)
        self.assertNotEqual(self.new_profile_1_data, self.new_profile_2_data)

    def test_views(self):
        self.client.login(username='admin', password=os.getenv('ADMIN_PASSWORD'), )
        self.new_profile_1_data['favorite_city'] = 'Versailles'
        response = self.client.post('/admin/profiles/profile/add/', self.new_profile_1_data,
                                    format='json', follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.get('/profiles/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
