from django.db import models
from django.contrib.auth.models import User

from .constants import UserRoles

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    name = models.CharField(max_length=128)
    role = models.IntegerField(choices=UserRoles.choices(), default=UserRoles.MAHASISWA)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
