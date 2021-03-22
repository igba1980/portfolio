# from django.contrib import admin
from django.urls import path
from . import views


app_name = 'job'

urlpatterns = [
    path('', views.joblist, name='job-list'),
    path('<int:pk>/', views.detail, name='detail')
]
