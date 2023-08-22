from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404

from .forms import *
from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'feedback'},
        {'title': "Контакты", 'url_name': 'contacts'},
        {'title': "Войти", 'url_name': 'login'}]

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
    }
    return render(request, 'wiki/post.html', context=context)

def show_category(request, cat_slug):
    posts = Wiki.objects.filter(cat__slug=cat_slug)
    if len(posts) ==0:
        raise Http404()
    cat = get_object_or_404(Category, slug=cat_slug)
    context = {
        'posts': posts,
        'menu': menu,
        'title': cat.name,
        'description': cat.description,

    }
    return render(request, 'wiki/category.html', context=context)

def about(request):
    return render(request,'wiki/about.html', {'menu': menu, 'title': 'О сайте'})

def feedback(request):
    return render(request,'wiki/feedback.html', {'menu': menu, 'title': 'Обратная связь'})

def contacts(request):
    return render(request,'wiki/contacts.html', {'menu': menu, 'title': 'Контакты'})

def login(request):
    return render(request,'wiki/login.html', {'menu': menu, 'title': 'Войти'})

def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()
    return render(request,'wiki/addpage.html', {'form': form, 'menu': menu, 'title': 'Добавление статьи'})

def archive(request, year):
    return HttpResponse(f"<h1>Архив по годам</h1><p>Архив за <b>{year}</b> год</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')