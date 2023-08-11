from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404

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

def show_post(request, post_slug):
    post = get_object_or_404(Wiki, slug=post_slug)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id,
    }
    return render(request, 'wiki/post.html', context=context)

def show_category(request, cat_slug):
    posts = Wiki.objects.filter(cat__slug=cat_slug)
    if len(posts) ==0:
        raise Http404()

    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': cat_slug,

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