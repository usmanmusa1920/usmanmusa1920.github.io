from django.urls import path
from .comment import Comment
from .reply import Reply


app_name = 'comment'

urlpatterns = [
    path("comment/<int:comment_id>/", Comment.comment, name='comment'),
    path("delete/comment/<int:comment_id>/", Comment.delete, name='delete'),
    path("mark/comment/<int:comment_id>/", Comment.markComment, name='mark'),
    
    # for reply
    path("delete/reply/<int:reply_id>/", Reply.delete, name='delete_reply'),
    path("mark/reply/<int:reply_id>/", Reply.markReply, name='mark_reply'),
]
