# from typing_extensions import Required
from django.db import models
from django.db.models.fields import EmailField

# Create your models here.


class UserProfile(models.Model):
    username = models.CharField(max_length=2000)
    age = models.IntegerField()
    email_address = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=90)
    profile_picture = models.ImageField(upload_to=None, blank=True)
    status = models.CharField(max_length=500)
    date_created = models.CharField(max_length=600)
    date_last_edited = models.CharField(max_length=500)
    otp_code = models.IntegerField()
    # pass





# foreign key solution 

# overriding the to_representation method in the serializer class 
# https://stackoverflow.com/questions/29950956/drf-simple-foreign-key-assignment-with-nested-serializers