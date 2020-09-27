from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('popular_tours/', views.tour, name='tours'),
    path('stories/', views.story, name='stories'),
    path('contact/', views.contact, name='contact'),
]