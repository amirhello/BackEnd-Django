#  we  create this file for api 
# api like cearte-reterv-updata-delete  CRUD
from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerialaizer(serializers.ModelSerializer):

    # We override the Meta class that exists in serializers.ModelSerializer
    class Meta:
        model = get_user_model()
        feilds = ("email" , "password" , "first_name" , "last_name")
    
    pass

