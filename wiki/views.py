from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect

from .models import *

menu = ["О сайте", "Добавить статью", "Обратная связь", "Контакты"]

def index(request):
    posts = Wiki.objects.all()
    return render(request,'wiki/index.html', {'posts': posts, 'menu': menu, 'title': 'Главная страница'})

def about(request):
    return render(request,'wiki/about.html', {'menu': menu, 'title': 'О сайте'})

def categories(request, cat):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>Категория <b>{cat}</b></p>")

def archive(request, year):
    return HttpResponse(f"<h1>Архив по годам</h1><p>Архив за <b>{year}</b> год</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')