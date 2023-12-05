# routing.py

from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from consumers import ChatConsumer
from django.core.asgi import get_asgi_application

application = ProtocolTypeRouter({
    "websocket": URLRouter(
        [
            path("ws/chat/<int:chatroom_id>/", ChatConsumer.as_asgi()),
            # Add any additional WebSocket paths here
        ]
    ),
    "http": get_asgi_application(),
})
