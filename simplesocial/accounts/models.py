from django.contrib import auth
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


POSITION_CHOICES=(
    ('prof','PROF'),
    ('stud', 'STUDENT'),
    ('alumnus','ALUMNUS'),
)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    position= models.CharField(max_length=255, choices=POSITION_CHOICES, default='stud')
    photo= models.ImageField(default= None)

    def str(self):
        return "@{}".format(self.user.username)


class User(auth.models.User, auth.models.PermissionsMixin):

   def str(self):
        return "@{}".format(self.username)