from django.shortcuts import get_object_or_404, render

from .models import Group, Post

CONST = 10


def index(request):
    posts = Post.objects.order_by('-pub_date')[:CONST]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.order_by('-pub_date')[:CONST]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
