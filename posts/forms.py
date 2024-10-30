from django import forms

from common.mixins import ReadOnlyMixin
from posts.models import Post


class BasePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


class DashBoardPage(BasePostForm):
    pass


class CreatePostForm(BasePostForm):
    class Meta:
        model = Post
        exclude = ['author']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Put an attractive and unique title...'}),
            'content': forms.Textarea(attrs={'placeholder': 'Share some interesting facts about your adorable pets...',
                                              })}
        labels = {
            'image_url': 'Put Image URL'}

class UpdatePostForm(BasePostForm):
    class Meta:
        model = Post
        exclude = ['author']
        labels = {
            'image_url': 'Put Image URL'}
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Put an attractive and unique title...'}), }
        help_texts = {
            'image_url': ''}


class DeletePostForm(ReadOnlyMixin, UpdatePostForm):
    read_only_fields = ['title', 'image_url', 'content']
