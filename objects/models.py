from django.db import models
from django.contrib.auth.models import User
from userauth.models import UserProfile


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=30)
    course_description = models.TextField(default='')
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_timestamp = models.DateTimeField(auto_now=True)

    created_by = models.OneToOneField(User, on_delete=models.CASCADE)

    @property
    def created_by_profile(self):
        name = UserProfile.objects.filter(user=self.created_by)[0]
        return name

    def __str__(self):
        return self.course_name


class Section(models.Model):
    id = models.AutoField(primary_key=True)
    section_name = models.CharField(max_length=30)
    section_description = models.TextField(default='')
    course_object = models.ForeignKey(Course,related_name="sections", on_delete=models.CASCADE)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_timestamp = models.DateTimeField(auto_now=True)

    created_by = models.OneToOneField(User, on_delete=models.CASCADE)

    @property
    def created_by_profile(self):
        name = UserProfile.objects.filter(user=self.created_by)[0]
        return name

    def __str__(self):
        return self.section_name


class Video(models.Model):
    id = models.AutoField(primary_key=True)
    video_title = models.CharField(max_length=30)
    video_duration_in_seconds = models.IntegerField(default=0)
    video_description = models.TextField(default='')
    video_file = models.FileField(upload_to='videos/', null=True, verbose_name="")
    section_object = models.ForeignKey(Section, on_delete=models.CASCADE,related_name="videos")
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_timestamp = models.DateTimeField(auto_now=True)

    created_by = models.OneToOneField(User, on_delete=models.CASCADE)

    @property
    def created_by_profile(self):
        name = UserProfile.objects.filter(user=self.created_by)[0]
        return name

    def __str__(self):
        return self.video_title

