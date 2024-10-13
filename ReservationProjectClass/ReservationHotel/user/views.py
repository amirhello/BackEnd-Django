from .serializers import UserSerializer
from rest_framework import generics
# generics has CRUD method that we can use it for api
#   


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    
