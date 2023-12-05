from django.contrib import admin

from .entity.message import Message
from .models import ChatRoom, ChatParticipant


# Register your models here.
admin.site.register(ChatRoom)
admin.site.register(ChatParticipant)
admin.site.register(Message)