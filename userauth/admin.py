from django.contrib import admin

# Register your models here.
from userauth.models import UserProfile

admin.site.register(UserProfile)
