from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import BlogPost
from .forms import BlogForm
from .check_blog_owner import check_blog_owner


@login_required
def index(request):
    """The home page for blogs and shows all blogs."""
    blogs = BlogPost.objects.filter(owner=request.user).order_by('date_added')
    context = {'blogs': blogs}
    return render(request, 'blogs/index.html', context)


@login_required
def new_blog(request):
    """Add a new blog post."""
    if request.method != 'POST':
        form = BlogForm()
    else:
        form = BlogForm(data=request.POST)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.owner = request.user
            new_blog.save()
            return redirect('blogs:index')

    context = {'form': form}
    return render(request, 'blogs/new_blog.html', context)


@login_required
def edit_blog_post(request, blog_id):
    blogs = BlogPost.objects.get(id=blog_id)
    check_blog_owner(blogs, request)
    if request.method != 'POST':
        form = BlogForm(instance=blogs)
    else:
        form = BlogForm(instance=blogs, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')

    context = {'blogs': blogs, 'form': form}
    return render(request, 'blogs/edit_blog_post.html', context)
