"""
ASGI config for WhatsApp project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from django.urls import path, re_path

from .consumers import ChatConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WhatsApp.settings')

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<chatroom_id>\d+)/$', ChatConsumer.as_asgi()),
]

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        'websocket': AuthMiddlewareStack(
            URLRouter(
                websocket_urlpatterns
            )
        ),
    }
)
