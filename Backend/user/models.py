from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from phone_field import PhoneField


# Create your models here.

class Puser(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    #additional
    address = models.CharField(blank=True, max_length=512)
    avatar = models.ImageField(
        max_length=255,
        upload_to ='profile_avatar/',default='profile_avatar/No_image_available.svg.png')
    # avatar = models.ImageField(upload_to='profile_pics', blank=True, default='profile_pics/defualt_avatar.png')
    phone = PhoneField(blank=True)


    def __str__(self):
        return self.user.username 

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Puser.objects.create(user=instance)
    
# @receiver(post_save, sender=User)
# def saver_user_profle(sender, instance, **kwargs):
#     instance.puser.save()
  
