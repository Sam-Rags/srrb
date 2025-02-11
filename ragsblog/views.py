from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from .forms import PostForm, ImageForm
from .models import Post, Image

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    imageform = ImageForm()
    images = Image.objects.filter(post=post)
    return render(request, 'post_detail.html', {'post': post, 'imageform': imageform, 'images': images,})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        files = request.FILES.getlist("image")
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            for i in files:
                Image.objects.create(post=post, image=i)
            messages.success(request, "New Post Added")
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
        imageform = ImageForm()
    return render(request, 'post_edit.html', {'form': form, "imageform": imageform})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
        imageform = ImageForm()
    return render(request, 'post_edit.html', {'form': form, "imageform": imageform})

@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('-created_date')
    return render(request, 'post_draft_list.html', {'posts': posts})

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method=='POST':
        post.publish()
    return redirect('post_detail', pk=pk)

@login_required
def post_unpublish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method=='POST':
        post.unpublish()
    return redirect('post_detail', pk=pk)


@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method=='POST':
        post.delete()
    return redirect('post_list')

def img_full(request, pk):
    imageform = get_object_or_404(ImageForm, pk=pk)
    return render(request, 'image_full.html', {'imageform': imageform})

