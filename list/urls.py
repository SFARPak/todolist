from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index, name ='index'),
    path('form/', views.form, name ='form'),
    path('user-profile/', views.user_profile, name='user_profile'),
    path('list-add/', views.list_add, name='list_add'),
    path('todo/<str:slug>', views.user_profile, name='user_profile'),
    path('todo/<str:slug>/edit/', views.list_update, name='list_update'),
    path('todo/<str:slug>/delete/', views.list_delete, name='list_delete'),
    path('login/', views.login_view, name ='login_view'),
    path('register/', views.register_view, name ='register_view'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    ]