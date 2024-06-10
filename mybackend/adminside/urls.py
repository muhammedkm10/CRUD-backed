from django.urls import path
from . import views
urlpatterns = [
    path('adminlogin',views.AdminLogin.as_view()),
    path('adduser',views.UserManagement.as_view()),
     path('adduser/<int:id>/',views.UserManagement.as_view()),
     path('adduser/edit/<int:id>/',views.UserManagement.as_view())

]
