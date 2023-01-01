from django import forms
from blog.models import Comment, Reply


class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ['full_name', 'email', 'text_body']
    
    
class ReplyForm(forms.ModelForm):
  class Meta:
    model = Reply
    fields = ['full_name', 'email', 'text_body']