from django.db import models
from django.contrib.auth.models import User


class ChatRoom(models.Model):
    name = models.CharField(max_length=100)
    max_count = models.IntegerField(default=1)
    total_members = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class ChatParticipant(models.Model):
    chat = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.chat.name
