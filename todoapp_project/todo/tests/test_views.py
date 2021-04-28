from django.test import TestCase, Client
from django.urls import reverse

import datetime

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.index_url = reverse('todoapp_project:todo:home')
        print(self.client)
        print(self.index_url)

    def test_project_index(self):
        response = Client.get(reverse(self.index_url))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, '')