from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name='projects'),
    path('project_details/<str:pk>/', views.project_details, name='project_details'),
    path('addproject/', views.addproject, name='addproject'),
    path('editproject/<str:pk>/', views.editproject, name='editproject'),
    path('deleteproject/<str:pk>/', views.deleteproject, name='deleteproject'),
    
]