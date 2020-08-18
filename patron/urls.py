from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.index,name='index'),
    path('search/', views.get_members,name='get_members')
] 