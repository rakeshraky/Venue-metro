from django.urls import path, include
from . import views



urlpatterns = [
    path('search/', views.get_members,name='get_members')
] 