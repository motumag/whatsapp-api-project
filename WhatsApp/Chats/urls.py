from django.urls import path
from rest_framework import permissions

from .controller import chatroom_controller
from .controller import message_controller
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="WhatsApp API",
        default_version='v1',
        description="implement whatsapp api using django drf",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="motumagishu27@gmail.com"),
        license=openapi.License(name="Motuma Licence"),
    ),
    public=True,
    permission_classes=([permissions.IsAuthenticated]),
)


urlpatterns = [
    path('chatrooms/', chatroom_controller.get_chatroom, name='chatroom-list'),
    path('chatrooms/create/', chatroom_controller.create_chatrooms, name='chatroom-create'),
    # path('chatrooms/<int:chatroom_id>/', chatroom_controller.get_chatroom, name='chatroom-detail'),
    path('chatrooms/leave/<int:chatroom_id>/', chatroom_controller.leave_chatroom, name='chatroom-leave'),
    path('chatrooms/update/<int:chatroom_id>/', chatroom_controller.update_chatroom, name='chatroom-update'),
    # path('chatrooms/<int:chatroom_id>/messages/', message_controller.list_messages, name='message-list'),
    path('chatrooms/<int:chatroom_id>/messages/create/', message_controller.CreateMessage.as_view({'post': 'create', 'get': 'list'}), name='create-message'),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
