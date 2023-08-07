from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contacts'},
        {'title': "Контакты", 'url_name': 'login'}]

def index(request):
    posts = Wiki.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница',

    }
    return render(request,'wiki/index.html', context=context)

def show_post(request, post_id):
    return HttpResponse(f'Отображение статьи с id {post_id}')

def show_category(request, cat_id):
    posts = Wiki.objects.filter(cat_id=cat_id)
    if len(posts) ==0:
        raise Http404()

    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': cat_id,

    }
    return render(request, 'wiki/index.html', context=context)

def about(request):
    return render(request,'wiki/about.html', {'menu': menu, 'title': 'О сайте'})

def contacts(request):
    return HttpResponse('Обратная связь')

def login(request):
    return HttpResponse('Авторизация')

def addpage(request):
    return HttpResponse('Добавить статью')

def categories(request, cat):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>Категория <b>{cat}</b></p>")

def archive(request, year):
    return HttpResponse(f"<h1>Архив по годам</h1><p>Архив за <b>{year}</b> год</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')