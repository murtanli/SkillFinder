from django.http import HttpResponse
from django.shortcuts import render
from .models import *

menu = {'login':'Войти','about':'О нас','work': 'Для рабочих','customer': 'Для заказчиков',}

def main(request):
    return render(request, 'works/osnova.html',context=menu)

def about(request):
    return render(request, 'works/about.html',context=menu)

def work(request):
    posts = profile.objects.all()
    return render(request, 'works/all.html', {'post':posts,'work': 'Для рабочих','customer': 'Для заказчиков',})

def show_post(request, post_id):
    posts = profile.objects.filter(pk=post_id)
    return render(request, 'works/post.html', {'post':posts, 'id':post_id})

def show_work(request):
    posts_wor = worker.objects.all()
    post_all = profile.objects.all()
    button = {
        'posts_wor': posts_wor,
        'post_all': post_all,
        'work': 'Для рабочих',
        'customer': 'Для заказчиков',
        'selected': 0,
        'title': 'Выбор рабочих',
    }
    return render(request, 'works/all_worker.html', context=button)

def show_cust(request):
    posts_cost = customer.objects.filter()
    post_all = profile.objects.all()
    button = {
        'posts_cost': posts_cost,
        'post_all': post_all,
        'work': 'Для рабочих',
        'customer': 'Для заказчиков',
        'selected': 1,
        'title': 'Выбор заказчиков',
    }
    return render(request, 'works/all_customer.html', context=button)