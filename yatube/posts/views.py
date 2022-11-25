from django.shortcuts import render, get_object_or_404
from .models import Post, Group

posts_amount: int = 10


def index(request):
    template = 'posts/index.html'
    posts = Post.objects.all()[:posts_amount]

    context = {
        'posts': posts,
    }

    return render(request, template, context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    template = 'posts/group_list.html'
    posts = group.posts.all()[:posts_amount]

    context = {
        'group': group,
        'posts': posts,
    }

    return render(request, template, context)
