from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_password, name='add_password'),
    path('view/<int:pk>/', views.view_password, name='view_password'),
]
