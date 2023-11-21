from django.urls import path
from app.views import *

urlpatterns = [
    path('', chat, name='home'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/',logout_user,name='logout')
]