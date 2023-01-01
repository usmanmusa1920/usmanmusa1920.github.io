from django.shortcuts import render
from account.default import default
from django.core.paginator import Paginator
from blog.models import Post


class Blog:
  """all blog post are here"""
  @staticmethod
  def blogs(request):
    post_all = Post.objects.all().order_by('-pub_date')
    
    paginator = Paginator(post_all, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    
    context = {
        'default': default(),
        'posts': posts,
    }
    return render(request, 'blog/blogs.html', context)