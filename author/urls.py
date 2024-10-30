from django.urls import path, include

from author.views import HomePage, CreateAuthorView, AuthorDetailsView, EditAuthorView, DeleteAuthorView

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('author/', include([
        path('create/', CreateAuthorView.as_view(), name='create-author'),
        path('details/', AuthorDetailsView.as_view(), name='author-details'),
        path('edit/', EditAuthorView.as_view(), name='edit-author'),
        path('delete/', DeleteAuthorView.as_view(), name='delete-author'),

    ]))
]