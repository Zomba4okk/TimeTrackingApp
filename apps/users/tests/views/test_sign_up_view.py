from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.users.models import User
from apps.users.tests.factories import UserFactory


class TestSignUpView(APITestCase):
    ENDPOINT_NAME = "signup"
    URL = reverse(ENDPOINT_NAME)

    def test_should_create_a_new_user(self):
        # assemble
        data = {
            "email": "a.b@gmail.com",
            "password": ":LKJ(87LKJBASD35!!",
            "first_name": "John",
            "last_name": "Smith",
        }
        assert not User.objects.filter(email=data["email"]).exists()

        # act
        response = self.client.post(self.URL, data=data)

        # assert
        assert response.status_code == status.HTTP_201_CREATED
        assert not response.data

        assert User.objects.filter(
            email=data["email"],
            first_name=data["first_name"],
            last_name=data["last_name"],
        ).exists()

    def test_should_return_400_when_fields_are_missed(self):
        # assemble
        data = {"email": "a.b@gmail.com", "password": ":LKJ(87LKJBASD35!!"}
        assert not User.objects.filter(email=data["email"]).exists()

        # act
        response = self.client.post(self.URL, data=data)

        # assert
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.json() == {
            "first_name": ["This field is required."],
            "last_name": ["This field is required."],
        }

    def test_should_return_400_when_email_is_already_in_user(self):
        # assemble
        user = UserFactory()
        data = {
            "email": user.email,
            "password": ":LKJ(87LKJBASD35!!",
            "first_name": "John",
            "last_name": "Smith",
        }

        # act
        response = self.client.post(self.URL, data=data)

        # assert
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.json() == {"email": ["user with this Email already exists."]}
