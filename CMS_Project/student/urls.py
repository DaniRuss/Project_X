from django.contrib import admin
from django.urls import path, include
from student import views


urlpatterns = [
    # this calling for student function form view
    path('', views.Student, name='student'), 
    # path('', views.view_students, name='view_students'),
    # path('home1/', views.home1, name='home1'),
]