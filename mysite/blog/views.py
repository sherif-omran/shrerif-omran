from django.shortcuts import render,  get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger 
from django.views.generic import ListView
# from .forms import EmailPostForm, CommentForm
from django.core.mail import send_mail
from django.views.decorators.http import require_POST

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post/list.html', {'posts': posts})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, status=Post.Status.PUBLISHED, 
                                slug=post,
                                publish__year=year, 
                                publish__month=month, 
                                publish__day=day
                            )
    return render(request, 'blog/post/detail.html', {'post': post})
