from django.http import HttpResponse
from django.shortcuts import render
from .models import *



def main(request):
    return HttpResponse("Главная страница")

def work(request):
    post = profile.objects.all()
    return render(request, 'works/all.html',{'post':post})