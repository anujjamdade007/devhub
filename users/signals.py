from django.contrib.auth.models import User
from .models import Profile
from django.db.models.signals import post_save, post_delete
from django.dispatch import Signal




#when user is created then automatic create profile with usename, email and name 
def createprofile(sender, instance , created , **kwargs):
    if created :
        user = instance
        profile = Profile.objects.create(
            user = user,
            username = user.username,
            email = user.email,
            name=user.first_name,
        )

def update_profile(sender , instance , created , **kwargs):
    profile = instance
    user = profile.user
    if created == False:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()



#when profile delete then automaticaly delete user
def deleteuser(sender, instance ,**kwargs):
    user = instance.user
    user.delete()

post_save.connect(createprofile , sender=User)
post_save.connect(update_profile , sender=Profile)
post_delete.connect(deleteuser , sender=Profile)