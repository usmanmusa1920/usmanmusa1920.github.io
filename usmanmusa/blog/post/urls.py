from django.urls import path, include
from .views import Post


app_name = 'post'

urlpatterns = [
    path("post/<int:post_id>/", Post.post, name='post'),
    path("post/update/<int:post_id>/", Post.update, name='update'),
    path("post/delete/<int:post_id>/", Post.delete, name='delete'),
]
