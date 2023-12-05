from ..repository.message_repository import MessageRepository


class MessageService:
    @staticmethod
    def get_messages_by_chatroom(chatroom_id):
        return MessageRepository.get_messages_by_chatroom(chatroom_id)

    @staticmethod
    def create_message(chatroom, sender, content):
        return MessageRepository.create_message(chatroom, sender, content)
