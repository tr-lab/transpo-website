
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import status
from rest_framework.serializers import Serializer

from biodata.models import UserProfile
from biodata.serializers import UserProfileSerializer



@api_view(['GET', 'POST'])
def user_profiles(request):
    # POST:
    # 1. Accept data and pass into serializer
    # 2. Validate the data
    # 3. Return error response if data not valid
    # 4. Save data if valid and return success response
    if request.method == "POST":
        serializer = UserProfileSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={"success":False, "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(data={"success": True, "data": serializer.data}, status=status.HTTP_201_CREATED)
    
    # pass