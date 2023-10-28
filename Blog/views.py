from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from . import forms as f
from .models import Post
from django.core.paginator import Paginator


@login_required(login_url= '../login/')
def NewBlogForm(request):
    form = f.PostForm(request.POST or None)
    
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user.username
        post.save()
        return redirect('profile/')

    dict = {
        'form': form,
    }
    return render(request, 'Blog/postform.html', dict)


@login_required(login_url= '../login/')
def UpdateBlogView(request, post_id=None):
    if post_id is None:
        post = None
    else:
        post = get_object_or_404(Post, id=post_id)
    if str(request.user) != str(post.author):
        return redirect('../../' + post.slug)
    form = f.PostForm(request.POST or None, instance=post)

    if form.is_valid():
        form.save()
        return redirect('../../'+ post.slug)

    context = {
        'form': form,
    }
    return render(request, 'Blog/updatepostform.html', context)


def DynamicBlogView(request, slug):
    obj = get_object_or_404(Post, slug = slug)

    context = {
        'post': obj,
        'curr_user': str(request.user),
        'author': str(obj.author),
    }
    return render(request, 'Blog/blog.html', context)


def BlogsView(request):
    query_set = Post.objects.filter(status = Post.Status.PUBLISHED)
    '''
        paginator = Paginator(query_set, 5)
        page = paginator.page(request.GET.get('page'))
    '''
    context = {
        'posts': query_set,
        'name': 'Blogs',
    }
    return render(request, 'Blog/blogs.html', context)


def ShooterView(request):
    posts = Post.objects.filter(genres__contains= 'Shooter', status = Post.Status.PUBLISHED)
    context = {
        'posts': posts,
        'name': 'Shooter',
        }
    return render(request, 'Blog/blogs.html', context)


def choice_matters_view(request):
    posts = Post.objects.filter(genres__contains= 'Choice Matters', status = Post.Status.PUBLISHED)
    context = {
        'posts': posts,
        'name': 'Choices Matters',
        }
    return render(request, 'Blog/blogs.html', context)


def adventure_view(request):
    posts = Post.objects.filter(genres__contains= 'Adventure', status = Post.Status.PUBLISHED)
    context = {
        'posts': posts,
        'name': 'Adventure',
        }
    return render(request, 'Blog/blogs.html', context)


def strategy_view(request):
    posts = Post.objects.filter(genres__contains='Strategy', status = Post.Status.PUBLISHED)
    context = {
        'posts': posts,
        'name': 'Strategy'
        }
    return render(request, 'Blog/blogs.html', context)


def BlogDeleteView(request, slug):
    obj = get_object_or_404(Post, slug = slug)
    if str(request.user) != str(obj.author):
        return redirect('../../' + obj.slug)
    
    if request.method == 'POST':
        obj.delete()
        return redirect('../../')
    context = {
        'obj' : obj,
    }
    return render(request, 'Blog/delete.html', context)
