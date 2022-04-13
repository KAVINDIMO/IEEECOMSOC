from asyncio import events
from http.client import HTTPResponse
from django.shortcuts import render,redirect

from main.forms import BLOG_FORM, EVENT_FORM, EVENT_REG, POSTS_FORM
from .models import *
# from django.views.generic import ListView

# Create your views here.

def Home(request):
    return render(request,"main/home.html",{})

def Events(request):
    obj = Event.objects.all()
    form = EVENT_REG(request.POST)
    if request.method == "POST":
        if form.is_valid():
            n = form.cleaned_data["name"]
            e = form.cleaned_data["event"]
            rg = form.cleaned_data["regno"]
            em = form.cleaned_data["email"]
            ph = form.cleaned_data["phone"]
            t = event_reg(name=n,event=e,regno=rg,email=em,phone=ph)
            t.save()
            return redirect("/")
        else:
            return redirect("/event")

    data = {
        'form':form,
        'obj':obj
    }
    return render(request,"main/event.html",data)

def PostView(request):
    obj = posts.objects.all()
    return render(request,"main/posts.html",{'obj':obj})

def BlogView(request):
    obj = blog.objects.all()
    return render(request,"main/blog.html",{'obj':obj})

def Event_upload(request):
    form = EVENT_FORM(request.POST,request.FILES)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            return redirect("/event")

    data = {
        'form':form
    }
    return render(request,"main/event_upload.html",data)

def post_upload(request):
    form = POSTS_FORM(request.POST,request.FILES,)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            return redirect("/posts")

    data = {
        'form':form
    }
    return render(request,"main/post_upload.html",data)

def blog_upload(request):
    form = BLOG_FORM(request.POST,request.FILES)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            return redirect("/blog")

    data = {
        'form':form
    }
    return render(request,"main/blog_upload.html",data)


