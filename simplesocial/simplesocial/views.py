from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

class TestPage(TemplateView):
    template_name = 'test.html'
    def get(self, request, *args, **kwargs):
        owner = self.request.user
        q=owner.username
        w=q.split('@')
        q=w[0]
        owner.username = q
        owner.save()
        return super().get(request, *args, **kwargs)

class TestPage2(TemplateView):
    template_name = 'test2.html'
    def get(self, request, *args, **kwargs):
        owner = self.request.user
        q=owner.username
        w=q.split('@')
        q=w[0]
        owner.username = q
        owner.save()
        return super().get(request, *args, **kwargs)

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

class HomePage(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("test"))
        return super().get(request, *args, **kwargs)
