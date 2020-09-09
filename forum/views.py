from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def showposts(req):
    posts = Post.objects.all()
    return render(req, 'forum/showposts.html', {'posts': posts})

def publishpost(req):
        if req.method == 'GET':
            if 'id' in req.GET.keys():
                id = req.GET['id']
                post = Post.objects.get(id=id)
                post.published = True
                post.save()
                return HttpResponse('published')


def unpublishpost(req):
        if req.method == 'GET':
            if 'id' in req.GET.keys():
                id = req.GET['id']
                post = Post.objects.get(id=id)
                post.published = False
                post.save()
                return HttpResponse('unpublished')



