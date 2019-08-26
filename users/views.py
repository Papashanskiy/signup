from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.urls import reverse_lazy


class SignUpView(generic.CreateView):
    template_name = 'signup.html'
    success_url = reverse_lazy('home')
    form_class = UserCreationForm
