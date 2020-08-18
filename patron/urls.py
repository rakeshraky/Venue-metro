from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.index,name='index'),
    path('api/search/', views.get_members,name='search')
] 