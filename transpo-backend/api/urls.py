
from django.urls import path 
from api.views.user_profile_views import user_profiles


urlpatterns = [
    path('userprofiles',  user_profiles, name="user_profiles")
]