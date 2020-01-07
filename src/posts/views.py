from django.shortcuts import render

# Create your views here.

from .models import Post


def posts_list(request):
    all_posts = Post.objects.all()
    context = {
        'all_posts': all_posts
    }
    return render(request, 'posts/posts_list.html', context)