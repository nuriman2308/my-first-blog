from django.shortcuts import render
from .models import Post # dot means current directory
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

# "logic" of our application

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
# request = everything we receive from the user via the Internet
