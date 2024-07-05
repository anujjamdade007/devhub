from django.urls import path
from . import views

urlpatterns = [
    path('', views.users, name='users'),
    path('user_profile/<str:pk>/' , views.user_profile , name='user_profile'),
    path('user_account/' , views.user_account , name='user_account'),
    path('update_profile/' , views.update_profile , name='update_profile'),


    path('login/' , views.userlogin , name='login'),
    path('register/' , views.registeruser , name='register'),
    path('logout/' , views.logoutuser , name='logout'),

    path('addskill/' , views.addskill , name='addskill'),
    path('editskill/<str:pk>/' , views.editskill , name='editskill'),
    path('deleteskill/<str:pk>/' , views.deleteskill , name='deleteskill'),

]