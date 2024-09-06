from django.urls import path
from .views import *
urlpatterns = [
    path('', homeHeroSection,name='home'),
]
