from django.shortcuts import render
from .models import Post
from django.utils import timezone
from .forms import PostForm
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404


# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk_var):
    post_instance = get_object_or_404(Post, pk=pk_var)
    return render(request, 'blog/post_detail.html', {'post_htm': post_instance})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail_name', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk_req_var): #what's pk?
    post = get_object_or_404(Post, pk=pk_req_var)
    if request.method == "POST":        # it seems to get here when 'save' is pressed. why?
        form = PostForm(request.POST, instance=post)
        
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
        
            return redirect('post_detail_name', pk_var=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})