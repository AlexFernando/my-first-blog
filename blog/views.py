from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') #name of my QuerySet
    return render(request,'blog/post_list.html', {'posts':posts})
    '''request is everything we receive from the user via the Internet, template file, {}, is a place in which we can add some things for the template to use. We need to give them names (we will stick to 'posts' right now)'''

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})

