from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from common.utils import get_current_author, get_specific_post
from posts.forms import DashBoardPage, CreatePostForm, UpdatePostForm, DeletePostForm
from posts.models import Post


# Create your views here.
class DashBoardView(ListView):
    model = Post
    form_class = DashBoardPage
    template_name = 'dashboard.html'


class CreatePostView(CreateView):
    model = Post
    template_name = 'create-post.html'
    form_class = CreatePostForm
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.author = get_current_author()
        return super().form_valid(form)


class PostDetailView(DetailView):
    template_name = 'details-post.html'
    model = Post

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Post.objects.filter(pk=pk)


class EditPostView(UpdateView):
    model = Post
    template_name = 'edit-post.html'
    success_url = reverse_lazy('dashboard')
    form_class = UpdatePostForm


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete-post.html'
    success_url = reverse_lazy('dashboard')
    form_class = DeletePostForm

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)

