from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

def index(request):
    return HttpResponse("Wiki main page")

def categories(request, cat):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>Категория <b>{cat}</b></p>")

def archive(request, year):
    return HttpResponse(f"<h1>Архив по годам</h1><p>Архив за <b>{year}</b> год</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')