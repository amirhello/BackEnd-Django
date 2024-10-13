from django.contrib.auth import get_user_model
from rest_framework import serializers

class RoomSerilizer(serializers.ModelSerializer):
    
    class Meta :
        model = get_user_model()
        fields =("hotel" ,"type" ) 
        
    