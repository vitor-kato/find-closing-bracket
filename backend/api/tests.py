from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import FindClosingBracket


class ModelTestCase(TestCase):
    """This class defines the test suite for the model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.string = "[]"
        self.index = 0
        self.bracket = FindClosingBracket(
            string=self.string, index=self.index)

    def test_model_can_create_a_bracket(self):
        """Test the bracket model can create a bracket."""
        old_count = FindClosingBracket.objects.count()
        self.bracket.save()
        new_count = FindClosingBracket.objects.count()
        self.assertNotEqual(old_count, new_count)


class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.data = {"string": "[ABC[23]][89]", "index": 0}
        self.response = self.client.post(
            reverse("create"), self.data, format="json")

    def test_api_can_create_a_bracket(self):
        """Test the api has bracket creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_bracket(self):
        """Test the api can get a given bracket."""
        bracket = FindClosingBracket.objects.get()
        response = self.client.get(
            reverse("detail", kwargs={"pk": bracket.id}), format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, bracket)

    def test_api_can_update_bracket(self):
        """Test the api can update a given bracket."""
        change_bracket = {"string": "[ABC[23]][89]", "index": 4}
        bracket = FindClosingBracket.objects.get()
        res = self.client.put(
            reverse("detail", kwargs={"pk": bracket.id}), change_bracket, format="json"
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_bracket(self):
        """Test the api can delete a bracket."""
        bracket = FindClosingBracket.objects.get()
        response = self.client.delete(
            reverse("detail", kwargs={"pk": bracket.id}), format="json", follow=True
        )
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
