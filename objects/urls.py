from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('course/', ListCourse.as_view(), name="course-list"),
    path('section/', ListSection.as_view(), name="section-list"),
    re_path('section/(?P<pk>[0-9]+)$', # Url to get update or delete a section
        get_delete_update_section.as_view(),
        name='get_delete_update_section'
    ),
    re_path('course/(?P<pk>[0-9]+)$',  # Url to get update or delete a course
            get_delete_update_course.as_view(),
            name='get_delete_update_course'
            )
]