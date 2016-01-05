from django.views import generic
from django.shortcuts import render
from django.utils import timezone

from .models import PostBlog


class BlogList(generic.ListView):
    template_name = "blog.html"
    context_object_name = 'blog_list'

    def get_queryset(self):
        return PostBlog.objects.order_by('-mudanca')


class BlogDetail(generic.DetailView):
    slug_field = 'titulo'
    model = PostBlog
    context_object_name = 'blog'
    template_name = 'blog_detail.html'

