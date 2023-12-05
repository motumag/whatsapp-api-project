from django.db import models
from .chatroom import ChatRoom
from django.contrib.auth.models import User


def user_directory_path(instance, filename):
    # This function generates the upload path for the file
    # For images
    return f'pictures/user_{instance.user.id}/{filename}'


def user_video_directory_path(instance, filename):
    # This function generates the upload path for the video file
    return f'videos/user_{instance.user.id}/{filename}'


class Message(models.Model):
    chat_room = models.ForeignKey(ChatRoom, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    content = models.TextField()
    picture = models.ImageField(upload_to=user_directory_path, null=True, blank=True)
    video = models.FileField(upload_to=user_video_directory_path, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
