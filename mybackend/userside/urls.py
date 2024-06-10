from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
  TokenObtainPairView,
)



urlpatterns = [
    
    path('api/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),


    path('userlist',views.ListUser.as_view(),name = 'userlist'),
    path('login',views.LoginByUser.as_view(),name = 'userlogin'),
    path('userdata',views.UserData.as_view())
]
