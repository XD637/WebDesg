from django.shortcuts import render,redirect
import requests
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import PostForm
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post

posts = [{"title": Post.title , "description": Post.description}]


# Create your views here.
def home(response):
    return render(response,"main/index.html")

def logout_request(response):
    logout(response)
    return redirect("/home")

@login_required(login_url="/login")
def feed(request):
    id = request.user.id
    posts = Post.objects.all().order_by("-created_at")
    context = {'post': posts}
    return render(request,"main/feed.html", context)

@login_required(login_url="/login")
def create_post(requests):
    if requests.method == "POST":
        form = PostForm(requests.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = requests.user
            post.save()
            return HttpResponseRedirect("/home")
    else:
        form = PostForm()
        return render(requests, "main/create_post.html", {"form":form})

def donate(response):
    return render(response,"main/donate.html")
    
def paypal(response):
    return render(response,"main/paypal.html")



