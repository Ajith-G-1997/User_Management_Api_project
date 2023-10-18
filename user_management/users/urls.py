from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,)


from .views import UserRegistration,UserProfileUpdateView,UserList

urlpatterns = [
    path('register/', UserRegistration.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    path('profile/', UserProfileUpdateView.as_view(), name='profile-update'),
    path('users/', UserList.as_view(), name='user-list'),
    
    
]
