from datetime import datetime

from django.db import models
from django.urls import reverse
# Create your models here.


class Guest(models.Model):

    guest_name = models.CharField(max_length = 100)
    email = models.EmailField(unique=True)


class GuestBookEntry(models.Model):
    
    knit_message = models.CharField(max_length = 140)
    extra_message = models.TextField()
    email = models.EmailField()
    name = models.CharField(max_length=250)
    date = models.DateTimeField(default=datetime.now())

    def get_absolute_url(self):
        return reverse('index')
