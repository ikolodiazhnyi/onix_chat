from django.contrib.auth.models import User
from django.db import models


class Room(models.Model):
    """
    A room for people to chat in.
    """
    title = models.CharField(max_length=64, unique=True)
    subscribers = models.ManyToManyField(User, related_name='rooms')

    def __str__(self):
        return self.title
