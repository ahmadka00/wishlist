from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save





class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False, blank=True)
    image_field = models.ImageField(default='wishlist/images/profile_default.png', upload_to='wishlist/images/users_profile/')
    def __str__(self):
        return self.user.username
    
class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    list_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return (
            f"{self.list_name} ({ '🟢'if self.is_active else '🔴'})"
        )

class Wish(models.Model):
    list_name = models.ForeignKey(Wishlist, related_name='wishs', on_delete=models.CASCADE)
    wish_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=200, blank=True )
    is_active = models.BooleanField(default=True)
    link= models.URLField(max_length=1000,blank=True)
    image = models.ImageField(upload_to='wishlist/images/wishes', blank=True, null=True)
    def __str__(self):
        return(
            f"{self.wish_name}"
            f"({self.created_at:%d-%m-%Y %H:%M}): "
            f"({ '🟢'if self.is_active else '🔴'})"
        )
    
    

@receiver(post_save, sender=User)
# sender can be removed if we will use the decorator @ receiver
def create_profile(instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        # Have the user follow themselves
        user_profile.followed_by.set([instance.profile.id])
        user_profile.save()
        