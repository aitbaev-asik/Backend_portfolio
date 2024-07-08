from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('projects/', views.projects, name='projects'),
    path('blog/new/', views.create_post, name='create_post'),
]
