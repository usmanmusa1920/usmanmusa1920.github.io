from django.urls import path
from .views import Message


app_name = 'message'

urlpatterns = [
    path("message/send/", Message.send, name='send'),
    path("mark/message/<int:msg_id>/", Message.markMessage, name='mark'),
    path("delete/message/<int:msg_id>/", Message.deleteMessage, name='delete'),
]
