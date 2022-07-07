from django.urls import path
from .views import (
	BlogCls,
	ArticleCls,
	PostCls,
	CommentCls,
	ReplyCls)


app_name = 'blog'

urlpatterns = [
	path('blog/', BlogCls.blogs, name='blog'),
	
	path('article/create/', ArticleCls.create, name='create_article'),
	path('article/<int:get_article>/', ArticleCls.article, name='article'),
	path('article/update/<int:get_article>/', ArticleCls.update, name='update_article'),
	
	path('post/<int:post_id>/', PostCls.post, name='post'),
	path('post/update/<int:post_id>/', PostCls.update, name='update_post'),
	path('post/delete/<int:post_id>/', PostCls.delete, name='delete_post'),
	
	path('comment/<int:comment_id>/', CommentCls.comment, name='comment'),
	path('delete/comment/<int:comment_id>/', CommentCls.delete, name='delete_comment'),
	path('mark/comment/<int:comment_id>/', CommentCls.mark, name='mark_comment'),
	
	path('delete/reply/<int:reply_id>/', ReplyCls.delete, name='delete_reply'),
	path('mark/reply/<int:reply_id>/', ReplyCls.mark, name='mark_reply'),
]
