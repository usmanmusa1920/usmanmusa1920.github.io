from django.urls import path, include
from .views import Article


app_name = 'article'

urlpatterns = [
    path("article/create/", Article.create, name='create'),
    path("article/<int:get_article>/", Article.article, name='article'),
    path("article/update/<int:get_article>/", Article.update, name='update'),
]
