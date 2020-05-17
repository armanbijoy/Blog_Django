from django.contrib import admin
from django.urls import path
from .views import RegistrationForm

urlpatterns = [
   path('registration/', RegistrationForm.as_view(), name='registration')
]