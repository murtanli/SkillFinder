from django.http import HttpResponse
from django.shortcuts import render

post = [1,2,3,4,5,6
]


def main(request):
    return HttpResponse("Главная страница")

def work(request):
    return render(request, 'works/all.html',{'post': post})