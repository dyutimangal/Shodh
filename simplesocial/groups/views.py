from django.contrib import messages
from django.contrib.auth.mixins import(
    LoginRequiredMixin,
    PermissionRequiredMixin
)


from django.urls import reverse, path
from django.db import IntegrityError
from django.shortcuts import get_object_or_404, render
from django.views import generic
from groups.models import Group
from . import models

def searchbar(request):
    if(request.method=="POST"):
        searched=request.POST.get("searchbar")
        field = request.POST.get("fieldofjob")
        # print(type(field))
        if field == 'all':
            groupss=Group.objects.filter(name__contains=searched)
        else :
            groupss=Group.objects.filter(name__contains=searched, field_of_job__contains =field)
        return render(request,'groups/searchbar.html',{'searched':searched, 'groupss':groupss})

class CreateGroup(LoginRequiredMixin, generic.CreateView):
    # fields = ("name", "description", "field_of_job")
    fields = ("name", "duration", "stipend", "location", "vacancy" ,"workstatus","description", "field_of_job", "expected_qualifications","apply_by", "start_date","additional_questions_to_applicant")

    model = Group
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.creator = self.request.user
        self.object.save()
        return super().form_valid(form)

class SingleGroup(generic.DetailView):
    model = Group

class ListGroups(generic.ListView):
    model = Group
 