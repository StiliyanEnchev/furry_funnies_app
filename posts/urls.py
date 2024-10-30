from django.urls import path, include

from posts.views import DashBoardView, CreatePostView, PostDetailView, EditPostView, DeletePostView

urlpatterns = [
    path('dashboard/', DashBoardView.as_view(), name='dashboard'),
    path('posts/', include([
        path('create/', CreatePostView.as_view(), name='create-post'),
        path('<int:pk>/details/', PostDetailView.as_view(), name='post-details'),
        path('<int:pk>/edit/', EditPostView.as_view(), name='edit-post'),
        path('<int:pk>/delete/', DeletePostView.as_view(), name='delete-post')

    ]))]