from django.contrib import admin

# Register your models here.
from objects.models import Course, Video, Section

admin.site.register(Course)
admin.site.register(Section)
admin.site.register(Video)
