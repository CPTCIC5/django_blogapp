from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse
from .models import Posts
from django.contrib import messages
from datetime import datetime
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    retrieve=Posts.objects.all()
    return render(request,'app1/index.html',{'retrieve':retrieve})

def detail(request,question_id):
    n1=Posts.objects.filter(pk=question_id)
    return render(request,'app1/detail.html',{"n1":n1})

def about(request):
    return render(request,'app1/about.html')

@login_required
def addpost(request):
    if request.method=='POST':
        title=request.POST.get('text')
        content=request.POST.get('content')
        print(title,content)
        current_time=datetime.now()
        n1=Posts(title=title,content=content,date_posted=current_time)
        n1.save()
        print(title,content)
        return HttpResponseRedirect('/')
    return render(request,'app1/posts.html')


@login_required
def delete_post(request,question_id):
    dele=Posts.objects.get(author=question_id)
    if dele.author == request.user:
        dele.delete()
    else:
        return render(request,'app1/index.html')
    return HttpResponseRedirect('/')