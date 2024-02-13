from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Snack

class SnackTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='caleb',
            password='hemphill123'
        )
        self.snack = Snack.objects.create(
            name='Test Snack',
            rating=5,
            reviewer=self.user
        )
    def test_list_page_status_code(self):
        url = reverse("snack_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    def test_list_page_template(self):
        url = reverse("snack_list")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "snack_list.html")
        self.assertTemplateUsed(response, "base.html")
    def test_detail_page_status_code(self):
        url = reverse("snack_detail", kwargs={'pk': self.snack.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    def test_detail_page_template(self):
        url = reverse("snack_detail", kwargs={'pk': self.snack.pk})
        response = self.client.get(url)
        self.assertTemplateUsed(response, "snack_detail.html")
        self.assertTemplateUsed(response, "base.html")