from django.db import models
import uuid
from users.models import Profile

# Create your models here.

class Project(models.Model):
    owner = models.ForeignKey(Profile , null=True , blank=True , on_delete= models.SET_NULL) 
    title = models.CharField(max_length = 200)
    description = models.TextField(null=True , blank=True)
    demo_link = models.CharField(max_length = 2000, null=True , blank=True )
    featured_image = models.ImageField(null=True , blank=True , default="default.jpg" , upload_to='images/')
    source_link = models.CharField(max_length = 2000, null=True , blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    vote_total = models.IntegerField(default=0 ,null=True , blank=True)
    vote_ratio = models.IntegerField(default=0 ,null=True , blank=True)
    created = models.DateTimeField(auto_now_add = True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4 , editable=False , unique=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['created']

    @property
    def reviewers(self):
        queryset = self.review_set.all().values_list('owner__id', flat = True)
        return queryset



class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote'),
    )
    owner = models.ForeignKey(Profile , null=True , blank=True , on_delete= models.SET_NULL)
    project = models.ForeignKey(Project , on_delete=models.CASCADE)
    body = models.TextField(null=True , blank=True)
    vote = models.CharField(max_length = 200 , choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add = True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4 , editable=False , unique=True)
    
    def __str__(self):
        return self.vote
    
    class Meta:
        unique_together = ['owner', 'project']
    
class Tag(models.Model):
    name = models.CharField(max_length = 200)
    created = models.DateTimeField(auto_now_add = True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4 , editable=False , unique=True)
    
    def __str__(self):
        return self.name

