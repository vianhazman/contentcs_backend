from rest_framework import serializers

from objects.serializers.video import VideoSerializer
from userauth.models import UserProfile
from objects.models import Section
from userauth.serializers import UserProfileSerializers
from userauth.constants import getAdminUser

class SectionSerializer(serializers.ModelSerializer):
    videos = VideoSerializer(many=True, read_only=True, allow_null=True)
    created_by_profile = serializers.SerializerMethodField('handle_admin', read_only=True)

    def handle_admin(self, obj):
        user = UserProfile.objects.filter(user=obj.created_by)
        if user.count() == 1:
            return UserProfileSerializers(user[0]).data
        return getAdminUser(obj.created_by.id)

    class Meta:
        model = Section
        fields = '__all__'

    def create(self, validated_data):
        return Section.objects.create(**validated_data)