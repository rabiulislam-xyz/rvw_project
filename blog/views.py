from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView

from blog.models import Post


class HomePageTemplate(TemplateView):
    template_name = 'blog/home_page.html'


class PostList(ListView):
    model = Post
    template_name = 'blog/post_list.html'


class PostDetail(DetailView):
    model = Post
    slug_url_kwarg = 'slug'
    template_name = 'blog/post_detail.html'

