from django.http import HttpResponse
from django.shortcuts import render
from .models import *



def main(request):
    return HttpResponse("Главная страница")

def work(request):
    post = profile.objects.all()
    return render(request, 'works/all.html',{'post':post})

def show_post(request, post_id):
    posts = profile.objects.filter(pk=post_id)
    return render(request, 'works/post.html', {'post':posts, 'id':post_id})

def show_work(request, work_id):
    posts = profile.objects.filter(pk=work_id)