from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.home,name="home"),
    path('signup', views.handleSignUp, name="handleSignUp"),
    path('login', views.handeLogin, name="handleLogin"),
    path('logout', views.handelLogout, name="handleLogout")
]