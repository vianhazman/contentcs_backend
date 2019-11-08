from django.urls import path, re_path
from .views import *
import userauth.views
from rest_framework_jwt.views import refresh_jwt_token

urlpatterns = [
    path('login', userauth.views.LoginView.as_view(), name='cas_ng_login'),
    path('logout', userauth.views.LogoutView.as_view(), name='cas_ng_logout'),
    path('ticket', userauth.views.CallbackView.as_view(), name='cas_ng_callback'),
    path('refresh', refresh_jwt_token,name="refresh_token"),

]