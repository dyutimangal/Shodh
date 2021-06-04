from django.views.generic.edit import UpdateView
from accounts.models import UserProfile
from accounts import models
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import (
  CreateView,
  DetailView,
  UpdateView


)
from django.views.generic.detail import DetailView
from django.shortcuts import render

from . import forms

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"

class profile(DetailView):
    models= models.UserProfile

    template_name= 'accounts/profile_detail.html' 
    queryset= UserProfile.objects.all()
    context = {
        "first_name": "Anjaneyulu",
        "last_name": "Batta",
        "address": "Hyderabad, India"
    }
    

class Editprofile(UpdateView):
    
    models= models.UserProfile
    template_name= 'accounts/editprofile.html' 
    print("debug")
    success_url='/groups/'
    queryset= UserProfile.objects.all()
    fields = ( "position", "photo","username")
    model = UserProfile

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()

        owner = self.request.user
        owner.save()
        return super().form_valid(form)