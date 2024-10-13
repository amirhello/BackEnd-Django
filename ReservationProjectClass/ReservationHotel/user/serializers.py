# We create this file for API 
# API for Create, Retrieve, Update, and Delete (CRUD)
from django.contrib.auth import get_user_model
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):

    # We override the Meta class that exists in serializers.ModelSerializer
    class Meta:
        model = get_user_model()
        fields = ("email", "password", "first_name", "last_name" ,"phone_number")  # Corrected spelling from "feilds" to "fields"
        # Fields are the attributes we work with in the serializer, 
        # and we use necessary fields like: "email", "password", "first_name", "last_name"

        # If we use this serializer to retrieve or read data through the API,
        # extra_kwargs will prevent the password from being included in the response.
        # The password can only be written, not read or displayed.
        extra_kwargs = {
            "password": {"min_length": 8, "write_only": True , "required":True}
        }
