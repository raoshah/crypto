from django.db import models

class UserPost(models.Model):
    username = models.CharField(max_length=60)
    userpost = models.CharField(max_length=1000)
