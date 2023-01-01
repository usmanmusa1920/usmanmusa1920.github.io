from django import forms
from blog.models import Post


class PostForm(forms.ModelForm):
  
  url_list_name = forms.CharField(max_length=255, required=False)
  url_list_value = forms.CharField(max_length=255, required=False)
  
  class Meta:
    model = Post
    fields = ['title', 'summary', 'image_url', 'snippet', 'url_list']