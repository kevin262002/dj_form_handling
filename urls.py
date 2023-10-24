from django.urls import path
from . import views

urlpatterns = [
    path('members/abc/', views.abc, name='abc'),
    path('members/', views.members, name='members'),
]