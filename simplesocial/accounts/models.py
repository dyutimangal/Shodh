from django.contrib import auth
from django.db import models
from django.utils import timezone

POSITION_CHOICES=(
    ('prof','PROF'),
    ('stud', 'STUDENT'),
    ('alumnus','ALUMNUS'),
)


class User(auth.models.User, auth.models.PermissionsMixin):
   position= models.CharField(max_length=255, choices=POSITION_CHOICES, default='stud')
   photo= models.ImageField(default= None)


   def __str__(self):
        return "@{}".format(self.username)
