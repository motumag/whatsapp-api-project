from ..repository.chatroom_repository import ChatRoomRepository


class ChatRoomService:
    @staticmethod
    def get_all_chatrooms():
        return ChatRoomRepository.get_all_chatrooms()

    @staticmethod
    def get_chatroom_by_id(chatroom_id):
        return ChatRoomRepository.get_chatroom_by_id(chatroom_id)

    @staticmethod
    def get_chatroom_by_id_user(user):
        return ChatRoomRepository.get_chatroom_by_id_user(user)

    @staticmethod
    def create_chatroom(name, user):
        # chat_instance = ChatRoomRepository.create_message()
        return ChatRoomRepository.create_chatroom(name, user)

    @staticmethod
    def update_chatroom(chatroom_id, user):
        return ChatRoomRepository.update_chatRoom(chatroom_id, user)

    @staticmethod
    def leave_chatroom(chatroom_id, user):
        return ChatRoomRepository.leave_chatRoom(chatroom_id, user)
