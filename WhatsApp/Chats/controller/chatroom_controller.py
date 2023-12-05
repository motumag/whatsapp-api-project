from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from ..serializers import ChatSerializer
from ..service.chatroom_service import ChatRoomService


@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def list_chatrooms(request):
    chatrooms = ChatRoomService.get_all_chatrooms()
    sender = request.user.id
    serializer = ChatSerializer(chatrooms, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_chatroom(request):
    user = request.user
    chatroom = ChatRoomService.get_chatroom_by_id_user(user)
    if not chatroom:
        return Response("not found", status=status.HTTP_404_NOT_FOUND)
    serializer = ChatSerializer(chatroom, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@authentication_classes([BasicAuthentication])  # Applying authentication
@permission_classes([IsAuthenticated])
def create_chatrooms(request):
    create = request.user
    name = request.data.get('name', '')
    if not name:
        return Response("name is required", status=status.HTTP_400_BAD_REQUEST)
    chat = ChatRoomService.create_chatroom(name, create)
    if chat == "duplicate":
        return Response("duplicate entry", status=status.HTTP_409_CONFLICT)
    serializer = ChatSerializer(chat)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def update_chatroom(request, chatroom_id):
    user = request.user
    chat = ChatRoomService.update_chatroom(chatroom_id, user)
    if not chat:
        return Response("not found", status=status.HTTP_404_NOT_FOUND)
    elif chat == "max":
        return Response("reached max user", status=status.HTTP_400_BAD_REQUEST)
    serializer = ChatSerializer(chat)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['DELETE'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def leave_chatroom(request, chatroom_id):
    user = request.user
    chat = ChatRoomService.leave_chatroom(chatroom_id, user)
    if not chat:
        return Response("not found", status=status.HTTP_404_NOT_FOUND)
    # serializer = ChatSerializer(chat)
    return Response("user left successfully", status=status.HTTP_200_OK)