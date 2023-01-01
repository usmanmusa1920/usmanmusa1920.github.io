from django import forms
from blog.models import Category


class CategoryForm(forms.ModelForm):
  
  url_list_name = forms.CharField(max_length=255, required=False)
  url_list_value = forms.CharField(max_length=255, required=False)
  
  class Meta:
    model = Category
    fields = ['title', 'description', 'image_url', 'snippet', 'url_list']