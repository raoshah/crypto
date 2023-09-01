from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import HttpResponseRedirect
from myapp.models import UserPost

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    userpost = UserPost.objects.all()
    if request.method == "POST": 
        username = request.POST["username"]
        post = request.POST["userpost"]
        post_add = UserPost(username=username, userpost=post)
        post_add.save()
        return HttpResponseRedirect(reverse("index"))
    return render(request, "myapp/index.html", {"userpost":userpost})


def login_user(request): 
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "myapp/login.html")
    return render(request, "myapp/login.html")

def register(request):
    return render(request, "myapp/register.html")

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))