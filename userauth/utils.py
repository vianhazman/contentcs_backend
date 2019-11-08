from .constants import UserRoles
from userauth.models import UserProfile

def get_logged_in_user_information(request):
    user = request.user
    userProfile = UserProfile.objects.filter(user=user.id)
    if (userProfile.count() == 1):
        return userProfile[0].role

def get_logged_in_user_object(request):
    user = request.user
    userProfile = UserProfile.objects.filter(user=user.id)
    if (userProfile.count() == 1):
        return userProfile[0]