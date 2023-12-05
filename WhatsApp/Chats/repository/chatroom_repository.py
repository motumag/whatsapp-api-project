from ..models import ChatRoom, ChatParticipant
from django.http import Http404

class ChatRoomRepository:
    @staticmethod
    def get_all_chatrooms():
        return ChatRoom.objects.all()

    @staticmethod
    def get_chatroom_by_id(chatroom_id):
        try:
            return ChatRoom.objects.get(pk=chatroom_id)
        except ChatRoom.DoesNotExist:
            return None

    @staticmethod
    def get_chatroom_by_id_user(user):
        try:
            print(ChatRoom.objects.filter(chatparticipant__user=user.id))
            return ChatRoom.objects.filter(chatparticipant__user=user.id)
        except ChatRoom.DoesNotExist:
            return None

    @staticmethod
    def get_chatparticipant_by_id(chatroom_id, user_id):
        try:
            return ChatParticipant.objects.get(chat=chatroom_id, user=user_id)
        except ChatParticipant.DoesNotExist:
            return None

    @staticmethod
    def create_chatroom(name, user):
        chat = ChatRoom.objects.get(name=name)
        if chat:
            return "duplicate"
        chat_instance = ChatRoom.objects.create(name=name)
        ChatParticipant.objects.create(chat=chat_instance, user=user)
        return chat_instance

    @staticmethod
    def update_chatRoom(chat_id, user):
        chat = ChatRoomRepository.get_chatroom_by_id(chat_id)
        if chat:
            if chat.total_members > chat.max_count:
                return "max"
            ChatParticipant.objects.create(chat=chat, user=user)
            chat.total_members = chat.total_members + 1
            chat.save()
            return chat
        else:
            return None

    @staticmethod
    def leave_chatRoom(chat_id, user):
        chat_participant = ChatRoomRepository.get_chatparticipant_by_id(chat_id, user)
        chat = ChatRoomRepository.get_chatroom_by_id(chat_id)
        if chat_participant and chat:
            chat.total_members = chat.total_members - 1
            chat.save()
            chat_participant.delete()
            return True
        return False
