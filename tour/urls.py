from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('home/', views.home, name='home'),
    path('popular_tours/', views.tour, name='tours'),
    path('stories/', views.story, name='stories'),
    path('contact/', views.contact, name='contact'),
]