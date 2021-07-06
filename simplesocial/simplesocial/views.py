from django import forms
from django.db.models.fields import BooleanField
from django.urls import reverse
from django.http import HttpResponseRedirect, request
from django.urls.base import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from accounts.models import UserProfile
from django.shortcuts import redirect, render


class CreateProfile(CreateView):
     
    models= UserProfile
    template_name='createprofile.html'   
    success_url='/test2/'
    queryset= UserProfile.objects.all()
    
    fields =( "position", "photo","username")

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()

        owner = self.request.user
        owner.save()
        return super().form_valid(form)
   


def sample_view(request):
  
    current_user = request.user
    temp = False
    if UserProfile.objects.filter(user=current_user).exists():
        temp = True

    if(temp):
        return redirect('/test2/')
    else:
        return redirect('/CreateProfile/')    

    print( current_user.username)
    

class TestPage(TemplateView ):
    
    
    template_name = 'test.html'
    def get(self, request, *args, **kwargs):
        owner = self.request.user
        q=owner.username
        w=q.split('@')
        q=w[0]
        owner.username = q
       ## owner.save()
        return super().get(request, *args, **kwargs)

class TestPage2(TemplateView):
    template_name = 'test2.html'
    def get(self, request, *args, **kwargs):
        owner = self.request.user
        q=owner.username
        w=q.split('@')
        q=w[0]
        owner.username = q
     ##   owner.save()
        return super().get(request, *args, **kwargs)

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

class HomePage(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("test"))
        return super().get(request, *args, **kwargs)
