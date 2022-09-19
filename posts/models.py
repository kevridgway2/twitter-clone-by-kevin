from django.db import models

from django import db
from cloudinary.models import CloudinaryField

# Create your models here.
class Post(models.Model):
    class Meta(object):
        db_table= 'post'
    
    name = models.CharField(
        'Name', blank=False, null=False,max_length=18,db_index=True, default='Anonymous',
    )
    body= models.CharField(
        'Body', blank=True, null=True, max_length=150,db_index=True
    )
    created_at = models.DateTimeField(
        'Created Datetime', blank=True,auto_now_add=True
    )
    image = CloudinaryField(
        'image', blank=True, db_index=True,
    )

    likes = models.PositiveIntegerField(
        'like', default=0,  blank=True, db_index=True,
    )