from .models import UserProfile
from rest_framework import serializers
from django.contrib.auth.models import User
from .constants import UserRoles

class UserProfileSerializers(serializers.ModelSerializer):

    role_name = serializers.SerializerMethodField('handle_role', read_only=True)

    def handle_role(self, obj):
        return UserRoles(obj.role).name

    class Meta:
        model = UserProfile
        fields = ['name','role','role_name','user']

class UserSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'