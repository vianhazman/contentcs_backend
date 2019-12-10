from rest_framework import serializers

from objects.serializers.section import SectionSerializer
from userauth.models import UserProfile
from objects.models import Course, Section, Video
from userauth.serializers import UserProfileSerializers
from django.forms.models import model_to_dict
from userauth.constants import getAdminUser
from django.shortcuts import get_list_or_404, get_object_or_404

class CourseSerializer(serializers.ModelSerializer):
    created_by_profile = serializers.SerializerMethodField('handle_admin',read_only=True)
    no_of_videos = serializers.SerializerMethodField('get_video_count',read_only=True)

    def handle_admin(self, obj):
        user = UserProfile.objects.filter(user=obj.created_by)
        if user.count() == 1:
            return UserProfileSerializers(user[0]).data
        return getAdminUser(obj.created_by.id)

    def get_video_count(self,obj):
        section = obj.sections.all()
        count = sum([i.videos.count() for i in section])
        return count
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