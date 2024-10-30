from author.models import Author
from posts.models import Post


def get_current_author():
    return Author.objects.first()


def get_post():
    return Post.objects.all()


def get_specific_post(self, pk):
    pk = self.kwargs.get('pk')
    return Post.objects.filter(pk=pk)