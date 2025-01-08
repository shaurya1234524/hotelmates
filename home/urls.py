from django.contrib import admin
from django.urls import path,include
from home  import views

urlpatterns = [
    path("", views.index,name='home'),
    path("about",views.about,name='about'),
    path("services",views.services,name='services'),
    path("search",views.search,name='search'),
    path('signup',views.handleSignup,name='handleSignup'),
    path('login',views.handlelogin,name='handlelogin'),
    path('logout',views.handlelogout,name='handlelogout'),
    path('contact',views.contact,name='contact')
]   