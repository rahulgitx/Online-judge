from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('contacts', views.contacts, name='contacts'),
    path('loginuser', views.loginuser, name='loginuser'),
    path('logoutuser', views.logoutuser, name='logoutuser'),
]