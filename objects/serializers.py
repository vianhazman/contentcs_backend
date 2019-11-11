from rest_framework import serializers
from .models import Course, Section, Video
from userauth.serializers import UserProfileSerializers

class VideoSerializer(serializers.ModelSerializer):
    created_by_profile = UserProfileSerializers(read_only=True)

    class Meta:
        model = Video
        fields = '__all__'

    def create(self, validated_data):
        return Video.objects.create(**validated_data)


class SectionSerializer(serializers.ModelSerializer):
    videos = VideoSerializer(many=True)
    created_by_profile = UserProfileSerializers(read_only=True)

    class Meta:
        model = Section
        fields = '__all__'

    def create(self, validated_data):
        return Section.objects.create(**validated_data)

class CourseSerializer(serializers.ModelSerializer):
    created_by_profile = UserProfileSerializers(read_only=True)

    class Meta:
        model = Course
        fields = '__all__'

    def create(self, validated_data):
        return Course.objects.create(**validated_data)

class CourseIndividualSerializer(serializers.ModelSerializer):
    sections = SectionSerializer(many=True)
    created_by_profile = UserProfileSerializers(read_only=True)

    class Meta:
        model = Course
        fields = '__all__'

    def create(self, validated_data):
        return Course.objects.create(**validated_data)


