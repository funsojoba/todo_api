from rest_framework.test import APITestCase
from django.urls import reverse


class TestTodos(APITestCase):
    def setUp(self):
        self.list_url = reverse('list todo')
        # self.single_todo = reverse('single todo')
        self.valid_payload = {
            "title": "test title",
            "description": "test description",
            "completed": "false"
        }

        self.invalid_payload = {
            "title": "",
            "description": "",
            "completed": ""
        }

    def test_list_todos(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)

    def test_valid_payload(self):
        response = self.client.post(self.list_url, data=self.valid_payload)
        self.assertEqual(response.status_code, 201)

    def test_invalid_payload(self):
        response = self.client.post(self.list_url, data=self.invalid_payload)
        self.assertEqual(response.status_code, 400)

