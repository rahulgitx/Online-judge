from django.contrib import admin
from django.urls import path, include
from problems import views

urlpatterns = [
    path('problem1', views.problem1func, name="problem1"),
    path('submitproblem1', views.submitproblem1, name="submitproblem1"),
    
]
