from django.shortcuts import render

from .models import PostBlog


def blog(request):
    blog_list = PostBlog.objects.all()
    return render(request, 'blog.html',  {'blog_list': blog_list})


def blog_detail(request, slug):
    blog = PostBlog.objects.get(slug=slug)
    return render(request, 'blog.html', {'blog': blog})
