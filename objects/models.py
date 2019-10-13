from django.db import models


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=30)
    course_description = models.TextField(default='')
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_timestamp = models.DateTimeField(auto_now=True)


class Section(models.Model):
    id = models.AutoField(primary_key=True)
    section_name = models.CharField(max_length=30)
    section_description = models.TextField(default='')
    course_object = models.ForeignKey(Course, on_delete=models.CASCADE)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_timestamp = models.DateTimeField(auto_now=True)


class Video(models.Model):
    id = models.AutoField(primary_key=True)
    video_title = models.CharField(max_length=30)
    video_duration_in_seconds = models.IntegerField(default=0)
    video_description = models.TextField(default='')
    video_file = models.FileField(upload_to='videos/', null=True, verbose_name="")
    section_object = models.ForeignKey(Section, on_delete=models.CASCADE)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_timestamp = models.DateTimeField(auto_now=True)
