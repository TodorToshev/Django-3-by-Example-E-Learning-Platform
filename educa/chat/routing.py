from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    #as_asgi() needed. https://channels.readthedocs.io/en/stable/releases/3.0.0.html
    re_path(r'ws/chat/room/(?P<course_id>\d+)/$', consumers.ChatConsumer.as_asgi()),
]
