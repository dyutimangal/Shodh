from django.conf import settings
from django.urls import reverse
from django.db import models

import misaka

from groups.models import  Group

from django.contrib.auth import get_user_model
User = get_user_model()
YEAR_CHOICES=(
    ('1','1st year'),
    ('2', '2nd year'),
    ('3','3rd year'),
    ('4','4th year'),
    ('na','Not Applicable'),
)
 
class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name="posts")
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)
    group = models.ForeignKey(Group,on_delete=models.CASCADE, related_name="posts",null=True, blank=True)
    name = models.CharField(max_length=255, default=None, null=True)    
    year = models.CharField(max_length=255, choices=YEAR_CHOICES, default='na', null=True)
    qualifications= models.TextField(blank=True, default='', null=True)
    def __str__(self):
        return self.message

    def save(self, *args, **kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            "posts:single",
            kwargs={
                "username": self.user.username,
                "pk": self.pk
            }
        )

    class Meta:
        ordering = ["-created_at"]
        unique_together = ["user", "message"]
