from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView

from author.forms import CreateAuthorForm, EditAuthorForm
from author.models import Author
from common.utils import get_current_author


# Create your views here.
class HomePage(TemplateView):
    template_name = 'index.html'

class CreateAuthorView(CreateView):
    model = Author
    form_class = CreateAuthorForm
    template_name = 'create-author.html'
    success_url = reverse_lazy('dashboard')

class AuthorDetailsView(DetailView):
    template_name = 'details-author.html'
    model = Author

    def get_object(self, queryset=None):
        return get_current_author()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        latest_post = self.object.posts.order_by('-updated_at').first()
        context['latest_post_title'] = latest_post.title if latest_post else None

        return context


class EditAuthorView(UpdateView):
    model = Author
    template_name = 'edit-author.html'
    form_class = EditAuthorForm
    success_url = reverse_lazy('author-details')

    def get_object(self, queryset=None):
        return get_current_author()

class DeleteAuthorView(DeleteView):
    model = Author
    template_name = 'delete-author.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return get_current_author()