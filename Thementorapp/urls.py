
from django.contrib import admin
from django.urls import path
from Thementorapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('starter/', views.starter, name='starter'),
    path('pricing', views.pricing, name='pricing'),
    path('courses', views.courses, name='courses'),
    path('details', views.details, name='details'),
    path('events', views.events, name='events'),
    path('trainers', views.trainers, name='trainers'),
    path('contact', views.contact, name='contact'),
]
