from django.views.generic import ListView, DetailView
from .models import Post

class NewsListView(ListView):
    model = Post
    template_name = 'default.html'
    context_object_name = 'news'
    ordering = ['-created_at']


class NewsDetailView(DetailView):
    model = Post
    template_name = 'default.html'
    context_object_name = 'post'