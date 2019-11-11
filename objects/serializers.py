from rest_framework import serializers

from userauth.models import UserProfile
from .models import Course, Section, Video
from userauth.serializers import UserProfileSerializers
from django.forms.models import model_to_dict
from userauth.constants import getAdminUser

class VideoSerializer(serializers.ModelSerializer):

    created_by_profile = serializers.SerializerMethodField('handle_admin', read_only=True)

    def handle_admin(self, obj):
        user = UserProfile.objects.filter(user=obj.created_by)
        if user.count() == 1:
            return UserProfileSerializers(user[0]).data
        return getAdminUser(obj.created_by.id)

    class Meta:
        model = Video
        fields = '__all__'

    def create(self, validated_data):
        return Video.objects.create(**validated_data)


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

class CourseSerializer(serializers.ModelSerializer):
    created_by_profile = serializers.SerializerMethodField('handle_admin',read_only=True)

    def handle_admin(self, obj):
        user = UserProfile.objects.filter(user=obj.created_by)
        if user.count() == 1:
            return UserProfileSerializers(user[0]).data
        return getAdminUser(obj.created_by.id)

    class Meta:
        model = Course
        fields = '__all__'

    def create(self, validated_data):
        return Course.objects.create(**validated_data)

class CourseIndividualSerializer(serializers.ModelSerializer):
    sections = SectionSerializer(many=True, read_only=True, allow_null=True)
    created_by_profile = serializers.SerializerMethodField('handle_admin', read_only=True)

    def handle_admin(self, obj):
        user = UserProfile.objects.filter(user=obj.created_by)
        if user.count() == 1:
            return UserProfileSerializers(user[0]).data
        return getAdminUser(obj.created_by.id)

    class Meta:
        model = Course
        fields = '__all__'

    def create(self, validated_data):
        return Course.objects.create(**validated_data)


