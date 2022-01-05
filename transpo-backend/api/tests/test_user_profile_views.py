
from django.urls import reverse

from api.views import user_profile_views

from django.contrib.auth import get_user_model
from rest_framework.test import APIClient, APITestCase


from biodata.models import UserProfile


User = get_user_model()


"""
UserProfileViewTest:
    - test_user_profile_success:
        - call api and pass in valid data
        - expect success to be True in the response json
        - expect new data in the db
        - expect values to be the same as data passed
    - test_user_profile_creation_failure"
        - call api and pass in invalid data
        - expect success to be False in the response json
        - expect no data created in the django db
"""

class UserProfileViewsTest(APITestCase):
    def setUp(self):
        self.client = APIClient()

        self.user_profile_author = User.objects.create(username="author@test.com", password="password@test.author")
        self.user_profile_data = {
            "username": self.user_profile_author.username,
            "age": 25,
            "email_address": self.user_profile_author.username,
            "phone_number" : "+234765423411",
            "status": "is active",
            "date_created": "13/24/2023",
            "date_last_edited": "15/14/2022",
            "otp_code":  7653,
        }
    
    def test_user_profile_success(self):
        """
            test_user_profile_success
        """
        response = self.client.post(reverse("user_profiles"), data=self.user_profile_data)
        self.assertEqual(response.status_code, 201)
        self.assertTrue(response.json()["success"])

        # Testing the data is created in the model 
        saved_user_profile = UserProfile.objects.get(username=self.user_profile_data["username"])
        self.assertTrue(saved_user_profile)

        # pass

    def test_user_profile_creation_failure(self):
        """
            test for user profile creatinon  failure when a field is empty 
        """
        data = self.user_profile_data
        del data["phone_number"]
        response = self.client.post(reverse("user_profiles"), data=data)
        self.assertEqual(response.status_code, 400)
        self.assertFalse(response.json()["success"])

        # Testing the data was not saved in the model 
        saved_user_profile = UserProfile.objects.all()
        self.assertEqual(len(saved_user_profile), 0)

        pass