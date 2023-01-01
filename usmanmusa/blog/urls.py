from django.urls import path, include
from .views import Blog


urlpatterns = [
    path("blog/", Blog.blogs, name='blogs'),
    path("", include('blog.article.urls')),
    path("", include('blog.post.urls')),
    path("", include('blog.comment.urls')),
]
