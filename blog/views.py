from itertools import zip_longest
from django.urls import reverse
from django.shortcuts import (
	render,
	redirect)
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from account.default import (
	integrate_mail,
	general_context,
	blog_url_processed)
from .forms import (
	PostForm,
	CommentForm,
	CategoryForm,
	ReplyForm)
from .models import (
	Post,
	Comment,
	Reply,
	Category)


class BlogCls:
	"""All blog post class"""

	@staticmethod
	def blogs(request):
		post_all = Post.objects.all().order_by('-pub_date')
		
		paginator = Paginator(post_all, 10)
		page = request.GET.get('page')
		posts = paginator.get_page(page)
		
		context = {
			'general_context': general_context(),
			'posts': posts,
		}
		return render(request, 'blog/blog.html', context)
	

class ArticleCls:
	"""
	Article class which include: creating, viewing, updating, and deleting an article.
	"""
	
	@login_required
	@staticmethod
	def create(request):
		"""This view handle the creation of an article"""
		
		if request.method == 'POST':
			form = CategoryForm(request.POST)
			if form.is_valid():
				url_list_name = form.cleaned_data.get('url_list_name')
				url_list_value = form.cleaned_data.get('url_list_value')
				list_1 = list(url_list_name.split(','))
				list_2 = list(url_list_value.split(','))
				url_list_data = list(zip_longest(list_1, list_2, fillvalue='Link'))
				
				instance = form.save(commit=False)
				instance.publisher = request.user
				
				# checking the form `url list` components
				if url_list_value == None or url_list_value == '' or url_list_name == None or url_list_name == '':
					instance.url_list = None
				else:
					instance.url_list = url_list_data
				instance.save()
				
				get_article = instance.id
				messages.success(request, f'You successfully create an article.')
				return redirect(reverse('blog:article', kwargs={'get_article': get_article}))
		else:
			form = CategoryForm()

		context = {
			'general_context': general_context(),
			'form': form
		}
		return render(request, 'blog/article_create.html', context)
	
	@staticmethod
	def article(request, get_article):
		"""
		This an article page, and also it include creating new post, where it will be in the article list of post.
		"""

		article = Category.objects.get(id=get_article)
		article_all = article.post_set.all().order_by('-pub_date')
		real_url = blog_url_processed(article)
		
		# here is the start tricks for creating post for this article
		if request.method == 'POST' and request.user.is_authenticated:
			form = PostForm(request.POST)
			if form.is_valid():
				url_list_name = form.cleaned_data.get('url_list_name')
				url_list_value = form.cleaned_data.get('url_list_value')
				list_1 = list(url_list_name.split(','))
				list_2 = list(url_list_value.split(','))
				url_list_data = list(zip_longest(list_1, list_2, fillvalue='Link'))
				
				instance = form.save(commit=False)
				instance.author = request.user
				instance.category = article
				
				# checking the form `url list` components
				if url_list_value == None or url_list_value == '' or url_list_name == None or url_list_name == '':
					instance.url_list = None
				else:
					instance.url_list = url_list_data
				instance.save()
				
				get_article = article.id
				messages.success(request, f'You successfully create a post.')
				return redirect(reverse('blog:article', kwargs={'get_article': get_article}))
			messages.warning(request, f'Something went bad while creating a post.')

		paginator = Paginator(article_all, 5)
		page = request.GET.get('page')
		article_post = paginator.get_page(page)

		context = {
			'general_context': general_context(),
			'article': article,
			'article_post': article_post,
			'real_url': real_url
		}
		return render(request, 'blog/article.html', context)
	
	@login_required
	@staticmethod
	def update(request, get_article):
		"""This is article update view"""

		article = Category.objects.get(id=get_article)
		real_url = blog_url_processed(article)
	
		if request.method == 'POST':
			form = CategoryForm(request.POST, instance=article)
			if form.is_valid():
				url_list_name = form.cleaned_data.get('url_list_name')
				url_list_value = form.cleaned_data.get('url_list_value')
				list_1 = list(url_list_name.split(','))
				list_2 = list(url_list_value.split(','))
				url_list_data = list(zip_longest(list_1, list_2, fillvalue='Link'))
				
				instance = form.save(commit=False)
				instance.publisher = request.user
				
				# checking the form `url list` components
				if url_list_value == None or url_list_value == '' or url_list_name == None or url_list_name == '':
					instance.url_list = None
				else:
					instance.url_list = url_list_data
				instance.save()
				
				get_article = instance.id
				messages.success(request, f'Successfully updated an article.')
				return redirect(reverse('blog:article', kwargs={'get_article': get_article}))
		else:
			form = CategoryForm(instance=article)
		context = {
			'general_context': general_context(),
			'form': form,
			'real_url': real_url
		}
		return render(request, 'blog/article_update.html', context)
	

class PostCls:
	"""Post class which include: creating, updating, and deleting a post"""
	
	@staticmethod
	def post(request, post_id):
		"""view for post page"""

		post = Post.objects.get(id=post_id)
		real_url = blog_url_processed(post)
		comments_all = post.comment_set.all().order_by('-timestamp')

		if request.method == 'POST':
			form = CommentForm(request.POST)
			if form.is_valid():
				instance = form.save(commit=False)
				instance.post = post

				sender_name = form.cleaned_data.get('full_name')
				sender_email = form.cleaned_data.get('email')
				text_body = form.cleaned_data.get('text_body')
				host, url_route = request.headers['Origin'], request.path_info
				integrate_mail(sender_name, sender_email, text_body, what='comment', _url_=f'{host}{url_route}')
				
				instance.save()
				messages.success(request, f'Thanks {sender_name} for your comment.')
				return redirect(reverse('blog:post', kwargs={'post_id': post_id}))
		else:
			form = CommentForm()

		paginator = Paginator(comments_all, 5)
		page = request.GET.get('page')
		post_comment = paginator.get_page(page)
		
		context = {
			'general_context': general_context(),
			'post': post,
			'post_comment': post_comment,
			'real_url': real_url
		}
		return render(request, 'blog/post.html', context)
	
	@login_required
	@staticmethod
	def update(request, post_id):
		"""View for updating a post"""

		post = Post.objects.get(id=post_id)
		real_url = blog_url_processed(post)
		
		if request.method == 'POST':
			form = PostForm(request.POST, instance=post)
			if form.is_valid():
				url_list_name = form.cleaned_data.get('url_list_name')
				url_list_value = form.cleaned_data.get('url_list_value')
				list_1 = list(url_list_name.split(','))
				list_2 = list(url_list_value.split(','))
				url_list_data = list(zip_longest(list_1, list_2, fillvalue='Link'))
				
				instance = form.save(commit=False)
				instance.publisher = request.user

			# checking the form `url list` components
			if url_list_value == None or url_list_value == '' or url_list_name == None or url_list_name == '':
				instance.url_list = None
			else:
				instance.url_list = url_list_data
			instance.save()
			
			messages.success(request, f'Post is updated.')
			return redirect(reverse('blog:post', kwargs={'post_id': post_id}))
		else:
			form = PostForm(instance=post)
		context = {
			'general_context': general_context(),
			'form': form,
			'real_url': real_url
		}
		return render(request, 'blog/post_update.html', context)
	
	@login_required
	@staticmethod
	def delete(request, post_id):
		"""View for deleting a post"""

		post = Post.objects.get(id=post_id)
		post_article_id = post.category.id
		post.delete()
		messages.success(request, f'You successfully deleted "{post.title}" post.')
		return redirect(reverse('blog:article', kwargs={'get_article':post_article_id}))
	

class CommentCls:
	"""Comment class, include: creating, deleting, and mark comment as read method."""
	
	@staticmethod
	def comment(request, comment_id):
		"""View handle comment page"""

		comment = Comment.objects.get(id=comment_id)
		reply_all = comment.reply_set.all().order_by('-timestamp')

		if request.method == 'POST':
			form = ReplyForm(request.POST)

			if form.is_valid():
				instance = form.save(commit=False)
				instance.comment = comment
				
				sender_name = form.cleaned_data.get('full_name')
				sender_email = form.cleaned_data.get('email')
				text_body = form.cleaned_data.get('text_body')
				host, url_route = request.headers['Origin'], request.path_info
				integrate_mail(sender_name, sender_email, text_body, what='reply', _url_=f'{host}{url_route}')

				instance.save()
				messages.success(request, f'Thanks {sender_name} for your reply.')
				return redirect(reverse('blog:comment', kwargs={'comment_id': comment_id}))
		else:
			form = ReplyForm()

		paginator = Paginator(reply_all, 5)
		page = request.GET.get('page')
		comment_reply = paginator.get_page(page)
		
		context = {
			'general_context': general_context(),
			'comment': comment,
			'comment_reply': comment_reply,
		}
		return render(request, 'blog/comment.html', context)
	
	@login_required
	@staticmethod
	def delete(request, comment_id):
		"""Delete comment view"""

		comment = Comment.objects.get(id=comment_id)
		comment.delete()
		messages.success(request, f'Successfully deleted 1 comment.')
		return redirect(reverse('auth:notification'))
	
	@login_required
	@staticmethod
	def mark(request, comment_id):
		"""Mark comment as read view"""

		comm = Comment.objects.get(id=comment_id)
		comm.is_read = True
		comm.save()
		messages.success(request, f'Successfully marked 1 comment as seen.')
		return redirect(reverse('auth:notification'))
	

class ReplyCls:
	"""Reply class, include creating, mark reply as read, and deleting a reply."""

	@login_required
	@staticmethod
	def delete(request, reply_id):
		"""Delete reply view"""

		reply = Reply.objects.get(id=reply_id)
		reply.delete()
		messages.success(request, f'Successfully deleted 1 reply.')
		return redirect(reverse('auth:notification'))
	
	@login_required
	@staticmethod
	def mark(request, reply_id):
		"""Mark reply as read view"""
		
		reply = Reply.objects.get(id=reply_id)
		reply.is_read = True
		reply.save()
		messages.success(request, f'Successfully marked 1 reply as seen.')
		return redirect(reverse('auth:notification'))
