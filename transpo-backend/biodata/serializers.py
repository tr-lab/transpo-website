
from rest_framework import serializers 
from .models import UserProfile


"""
UserProfileSerializer :
  - all fields 
  - accept default validation (django models)

"""

class UserProfileSerializer(serializers.ModelSerializer):
  
    class Meta:
      model = UserProfile 
      # all fields in UserProfile db such as user name age 
      fields = "__all__"
