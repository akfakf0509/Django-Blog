from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post, Comment


def home(request):
    posts = Post.objects

    return render(request, 'home.html', {'posts': posts})


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = list(Comment.objects.filter(post_id=post_id))

    if comments:
        return render(request, 'detail.html', {'post': post, 'comments': comments})
    else:
        return render(request, 'detail.html', {'post': post})


def write(request):
    return render(request, 'write.html')


def create_comment(request, post_id):
    comment = Comment()
    comment.post_id = get_object_or_404(Post, pk=post_id)
    comment.date = timezone.datetime.now()
    comment.content = request.GET['content']
    comment.likes = 0
    comment.save()

    return redirect('/post/' + str(post_id))


def create(request):
    if request.GET['password'] == 'admin1234':
        post = Post()
        post.title = request.GET['title']
        post.content = request.GET['content']
        post.date = timezone.datetime.now()
        post.likes = 0
        post.save()

    return redirect('/')
