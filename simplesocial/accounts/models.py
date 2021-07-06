from django.contrib import auth
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify
from groups.models import  Group


POSITION_CHOICES=(
    ('prof','Faculty'),
    ('stud', 'Student'),
    ('alumnus','Alumnus'),
)
GENDER_CHOICES=(
    ('anon','Prefer Not To Say'),
    ('m', 'Male'),
    ('f','Female'),
)
BRANCH_CHOICES=( 
('bt','Biotech'), 
('ch', 'Chemical'), 
('cse','Computer Science'), 
('mnc','Mathematics'), 
('ep','Engineering Physics'),
('ece','Electronics'),
('ee','Electrical'),
('me','Mechanical'),
('cv','Civil'),
('cst','CST') 
)

class UserProfile(models.Model):
    name = models.CharField(default=None,max_length=256,null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    slug = models.SlugField(allow_unicode=True, unique=True,  default=None)
    position= models.CharField(max_length=255, choices=POSITION_CHOICES, default='stud')
    photo= models.ImageField(default= None,null=True)
    username = models.CharField(max_length=256)
    aboutme = models.TextField(default=None,null=True)
    branch = models.CharField(max_length=255, choices=BRANCH_CHOICES, default='bt')
    cpi = models.FloatField(default=None,null=True)
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES, default='anon')
    linkedin = models.CharField(default=None,max_length=256,null=True)
    # resume = models.FileField(default=None,null=True)
    
    def save(self, *args, **kwargs):
        kc = self.username
        print(kc)
        self.slug = slugify(kc)
        super().save(*args, **kwargs)


class User(auth.models.User, auth.models.PermissionsMixin):

   def str(self):
        return "@{}".format(self.username)