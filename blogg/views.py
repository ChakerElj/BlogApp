from django.shortcuts import render
from django.views.generic import ListView, DetailView

# Create your views here.
from blogg.models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'post_list'


class BlogView(DetailView):
    model = Post
    template_name = 'post_detail.html'