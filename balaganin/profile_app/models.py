from django.db import models
from django.contrib.auth.models import User
from django.contrib.admin import options
from datetime import datetime
import birthday
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=20, null=True)
    city = models.CharField(max_length=50, null=True)
    image = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'



@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        profile = Profile(user=instance)
        profile.save()