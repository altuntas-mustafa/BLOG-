from dataclasses import field
from .models import Post, Comment
from django import forms


class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ['title','content','category','status']

class ShowForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ['title','content','created_at','updated_at']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)