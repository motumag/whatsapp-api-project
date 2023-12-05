# from WhatsApp.Chats.repository.message_repository import MessageRepository
from rest_framework import status, generics, viewsets, permissions
from rest_framework.exceptions import NotFound
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.decorators import api_view, api_view, authentication_classes, permission_classes
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.views.decorators.csrf import csrf_exempt

from ..entity.message import Message
from ..serializers import MessageSerializer
from ..service.message_service import MessageService
from ..service.chatroom_service import ChatRoomService

# @api_view(['GET'])
# @authentication_classes([BasicAuthentication])
# @permission_classes([IsAuthenticated])
# def list_messages(request, chatroom_id):
#     messages = MessageService.get_messages_by_chatroom(chatroom_id)
#     serializer = MessageSerializer(messages, many=True)
#     # Serialize messages if needed
#     return Response(serializer.data, status=status.HTTP_200_OK)


class CreateMessage(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly]
    authentication_classes([BasicAuthentication])

    def get_queryset(self):
        chatroom_id = self.kwargs.get('chatroom_id')
        if chatroom_id:
            return MessageService.get_messages_by_chatroom(chatroom_id)
        else:
            return None

    def perform_create(self, serializer):
        chatroom_id = self.kwargs.get('chatroom_id')
        chatroom = ChatRoomService.get_chatroom_by_id(chatroom_id)

        if chatroom is None:
            raise NotFound("Chatroom not found")

        serializer.save(user=self.request.user, chat_room=chatroom)
        channel_layer = get_channel_layer()
        message_data = {
            'type': 'chat.message',
            'message': serializer.data,
        }

        async_to_sync(channel_layer.group_send)(
            f"chat_{chatroom_id}",
            message_data
        )