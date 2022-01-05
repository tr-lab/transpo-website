
from django.test import TestCase
from django.contrib.auth import get_user_model

from biodata.models import UserProfile

User = get_user_model()


    

class UserProfileTest(TestCase):
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
            "otp_code":  7653,
            
        }
    
    def test_object_creation(self):
        """
            Test that the sample user profile 
            can be created in the db returns: 
        """

        user_profile = UserProfile.objects.create(**self.user_profile_data)
        self.assertEqual(user_profile.username, self.user_profile_data["username"])
        self.assertEqual(user_profile.age, self.user_profile_data["age"])
        self.assertEqual(user_profile.email_address, self.user_profile_data["email_address"])
        self.assertEqual(user_profile.phone_number, self.user_profile_data["phone_number"])
        self.assertEqual(user_profile.status, self.user_profile_data["status"])
        self.assertEqual(user_profile.date_created, self.user_profile_data["date_created"])
        self.assertEqual(user_profile.date_last_edited, self.user_profile_data["date_last_edited"])
        self.assertEqual(user_profile.otp_code, self.user_profile_data["otp_code"])


    # pass

   