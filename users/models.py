from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.



class Profile(models.Model):
    user = models.OneToOneField(User ,on_delete=models.CASCADE , null=True , blank=True)
    name =  models.CharField(max_length = 200, null=True , blank=True )
    email = models.EmailField(max_length = 200, null=True , blank=True)
    username =  models.CharField(max_length = 200, null=True , blank=True )
    headline =  models.CharField(max_length = 200, null=True , blank=True )
    bio = models.TextField(null=True , blank=True)
    location = models.CharField(max_length = 200, null=True , blank=True )
    profile_image = models.ImageField(null=True , blank=True , default="user-default.png" , upload_to='userprofile/')
    social_github = models.CharField(max_length = 2000, null=True , blank=True)
    social_twitter = models.CharField(max_length = 2000, null=True , blank=True)
    social_linkedin = models.CharField(max_length = 2000, null=True , blank=True)
    social_youtube = models.CharField(max_length = 2000, null=True , blank=True)
    social_website = models.CharField(max_length = 2000, null=True , blank=True)
    created = models.DateTimeField(auto_now_add = True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4 , editable=False , unique=True)

    def __str__(self):
        return str(self.user.username )
    
    class Meta:
        ordering = ['created']
    


class Skills(models.Model):
    owner = models.ForeignKey(Profile , on_delete=models.CASCADE , null=True , blank=True)
    name = models.CharField(max_length = 200, null=True , blank=True )
    description = models.TextField(null=True , blank=True)
    created = models.DateTimeField(auto_now_add = True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4 , editable=False , unique=True)
    

    def __str__(self):
        return str(self.name)
    
