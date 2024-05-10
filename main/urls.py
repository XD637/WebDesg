from django.urls import path
from . import  views

urlpatterns = [
    path('', views.home, name = "home"),
    path('home/', views.home, name = "home"),
    path('feed/', views.feed, name = "feed"),
    path('post/', views.create_post, name = "create_post"),
    path("logout/", views.logout_request, name="logout"),
    path('donate/', views.donate, name = "donate"),
    path('paypal/', views.paypal, name = "paypal"),
]
