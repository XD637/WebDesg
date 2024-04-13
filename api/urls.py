from django.urls import path
from .import views

urlpatterns = [
    path('api', views.getData,name="getData"),
    path('api/post', views.createPost,name="createPost"),
]