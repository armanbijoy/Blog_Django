from django.shortcuts import render
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.urls import reverse_lazy
# Create your views here.
class RegistrationForm(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
   
    success_url = reverse_lazy('login')