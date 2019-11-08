from .models import UserProfile
from rest_framework import serializers
from django.contrib.auth.models import User

class UserProfileSerializers(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = '__all__'

class UserSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'