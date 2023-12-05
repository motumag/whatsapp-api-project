# consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.chatroom_id = self.scope['url_route']['kwargs']['chatroom_id']
        self.chatroom_group_name = f"chat_{self.chatroom_id}"

        # Join room group
        await self.channel_layer.group_add(
            self.chatroom_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.chatroom_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # Receive message from WebSocket
        print("receive called")
        data_json = json.loads(text_data)
        message = data_json['message']
        print("received", message)
        # Broadcast message to room group
        await self.channel_layer.group_send(
            self.chatroom_group_name,
            {
                'type': 'chat.message',
                'message': message
            }
        )

    async def chat_message(self, event):
        # Send message to WebSocket
        print("called")
        message = event['message']
        print("message", message)
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
