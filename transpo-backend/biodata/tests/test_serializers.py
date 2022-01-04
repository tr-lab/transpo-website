

from django.test import TestCase

from django.contrib.auth import get_user_model
from rest_framework import serializers

from biodata.serializers import UserProfileSerializer
from biodata.models import UserProfile


User = get_user_model()


class UserProfileSerializerTest(TestCase):
    def setUp(self):
        self.user_profile_author = User.objects.create(username="author@test.com", password="password@test.author")
        self.user_profile_data = {
            "username": self.user_profile_author.username,
            "age": 25,
            "email_address": self.user_profile_author.username,
            "phone_number" : "+234765423411",
            "status": "is active",
            "date_created": "13/24/2023",
            "date_last_edited": "15/14/2022",
            "otp_code":  "7653",
        }
        
        self.required_error_msg = "This field is required."


    def test_validation_true(self):
        """
        Test if that the serializer is valid, right data is passed to the serializer 
        and the right data is saved 
        returns 
        """ 
        serializer = UserProfileSerializer(data=self.user_profile_data)
        self.assertTrue(serializer.is_valid())

        # Test save()
        user_profile = serializer.save()

        # first Test that data is saved == data passed
        for field in self.user_profile_data:
            self.assertEqual(eval(f"user_profile.{field}"), self.user_profile_data.get(field))

        saved_user_profile = UserProfile.objects.get(username=self.user_profile_data["username"])
        self.assertEqual(saved_user_profile, user_profile)

         



