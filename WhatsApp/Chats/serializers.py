from django.contrib.auth.models import User

from .entity.chatroom import ChatParticipant
from .models import ChatRoom, Message
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')  # Add more fields as needed


class ChatParticipantSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = ChatParticipant
        fields = ('user',)  # Add other fields if needed


class ChatSerializer(serializers.ModelSerializer):
    participants = ChatParticipantSerializer(many=True, source='chatparticipant_set')

    class Meta:
        model = ChatRoom
        fields = ('id', 'name', 'participants',)


class MessageSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.id')
    chat_room = serializers.ReadOnlyField(source='chatroom.id')
    picture = serializers.ImageField(required=False)
    video = serializers.FileField(required=False
                                  )

    class Meta:
        model = Message
        fields = ['id', 'user', 'chat_room', 'content', 'picture', 'video', 'timestamp']
