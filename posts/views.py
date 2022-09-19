from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else: 
            return HttpResponseRedirect(form.errors.as_json())
    posts = Post.objects.all().order_by('-created_at')[:20]
    return render(request,"posts.html",{'posts':posts})

def edit(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect(form.errors.as_json())
    form = PostForm
    return render(request, 'edit.html', {'post': post, 'form': form})

def delete(request,post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')
    output = 'POST ID IS' + str(post_id)
    return HttpResponse(output)


def LikeView(request,post_id):
    post = Post.objects.get(id = post_id)
    new_value=post.likes + 1
    post.likes = new_value
    post.save()
    return HttpResponseRedirect('/')