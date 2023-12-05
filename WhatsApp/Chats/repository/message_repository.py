from ..models import Message


class MessageRepository:
    @staticmethod
    def get_messages_by_chatroom(chatroom_id):
        return Message.objects.filter(chat_room_id=chatroom_id)

    @staticmethod
    def create_message(chatroom, sender, content):
        return Message.objects.create(chat_room=chatroom, sender=sender, content=content)
