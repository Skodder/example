from django.views.generic.list import ListView
from post.models import Post


class PostListView(ListView):
    model = Post
    template_name = "post/post_list.html"

    PERSON_FIELD = "person"
    TITLE_FIELD = "title"
    BODY_FIELD = "body"
    
    def get_queryset(self):
        qs = self.model.objects.all()
        request = self.request
        get_data = request.GET.copy()
        current_field = get_data.get("field", None)
        if current_field is None:
            return qs

        request_value = get_data.get("value", "NONE")
        if current_field == self.PERSON_FIELD:
            return qs.filter(person__name__icontains=request_value)
        elif current_field == self.TITLE_FIELD:
            return qs.filter(title__icontains=request_value)
        elif current_field == self.BODY_FIELD:
            return qs.filter(body__icontains=request_value)

        return qs
