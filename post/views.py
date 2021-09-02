from django.views.generic.list import ListView
from post.models import Post


class PostListView(ListView):
    model = Post
    template_name = "post/post_list.html"

    def get_queryset(self):
        return self.model.objects.all()
