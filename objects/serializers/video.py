from rest_framework import serializers

from userauth.models import UserProfile
from objects.models import Course, Section, Video
from userauth.serializers import UserProfileSerializers
from userauth.constants import getAdminUser

class VideoCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'course_name')

class VideoSectionSerializer(serializers.ModelSerializer):
    course_object = VideoCourseSerializer()
    class Meta:
        model = Section
        fields = ('id', 'section_name', 'course_object')


class VideoSerializer(serializers.ModelSerializer):

    created_by_profile = serializers.SerializerMethodField('handle_admin', read_only=True)
    section_object = VideoSectionSerializer()

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

