from django.conf import settings
from django.urls import reverse
from django.db import models
from django.utils.text import slugify


import misaka

from django.contrib.auth import get_user_model
User = get_user_model()

from django import template
register = template.Library()

FIELD_CHOICES=(
    ('ml','ML'),
    ('appd', 'APPD'),
    ('webdf','WEBDF'),
    ('webdb','WEBDB'),
    ('sde','SDE'),
)

SKILL_CHOICES=(
    ('react','REACT'),
    ('python', 'PYTHON'),
    ('java','JAVA'),
    ('django','DJANGO'),
    ('js','JS'),
)

class Group(models.Model):
    creator = models.ForeignKey(User,on_delete=models.CASCADE, related_name="group_creator")
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(blank=True, default='')
    description_html = models.TextField(editable=False, default='', blank=True)
    #cpi_cutoff = models.DecimalField(max_digits=3, decimal_places=2)
    field_of_job= models.CharField(max_length=255, choices=FIELD_CHOICES, default='sde')
    skills_required=models.CharField(max_length=255,choices=SKILL_CHOICES, default='js')
    duration = models.TextField(blank=True, default='', null=True)
    stipend = models.TextField(blank=True, default='', null=True)
    expected_qualifications= models.TextField(blank=True, default='', null=True)
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("groups:single", kwargs={"slug": self.slug})


    class Meta:
        ordering = ["name"]

