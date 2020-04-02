from django.db import models
from datetime import datetime


class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField(default=datetime.now)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
