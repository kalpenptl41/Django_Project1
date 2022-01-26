from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='HomePage-home'),
    path('about/', views.about, name='HomePage-about'),
]