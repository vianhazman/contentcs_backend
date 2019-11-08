from rest_framework import permissions
from .constants import UserRoles
from .utils import get_logged_in_user_information

SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS']

class IsMahasiswa(permissions.BasePermission):
    def has_permission(self, request, view):
        return get_logged_in_user_information(request) == UserRoles.MAHASISWA and request.method in SAFE_METHODS

class IsDosen(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return get_logged_in_user_information(request) == UserRoles.DOSEN

    def has_permission(self, request, view):
        return get_logged_in_user_information(request) == UserRoles.DOSEN



