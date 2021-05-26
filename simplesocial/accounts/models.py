from django.contrib import auth
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify
from groups.models import  Group


POSITION_CHOICES=(
    ('prof','PROF'),
    ('stud', 'STUDENT'),
    ('alumnus','ALUMNUS'),
)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    slug = models.SlugField(allow_unicode=True, unique=True,  default=None)
    position= models.CharField(max_length=255, choices=POSITION_CHOICES, default='stud')
    photo= models.ImageField(default= None)

    job1 =  models.ForeignKey(Group,on_delete=models.SET_NULL , related_name="job1", default=None, null=True)
    job2 =  models.ForeignKey(Group,on_delete=models.SET_NULL , related_name="job2", default=None, null=True)
    job3 =  models.ForeignKey(Group,on_delete=models.SET_NULL , related_name="job3", default=None, null=True)



    def str(self):
        return "@{}".format(self.user.username)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super().save(*args, **kwargs)


class User(auth.models.User, auth.models.PermissionsMixin):

   def str(self):
        return "@{}".format(self.username)