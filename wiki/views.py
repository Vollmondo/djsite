from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from .forms import *
from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'feedback'},
        {'title': "Контакты", 'url_name': 'contacts'},
        {'title': "Войти", 'url_name': 'login'}]

class WikiMain(ListView):
    model = Wiki
    template_name = 'wiki/index.html'
    context_object_name = 'posts'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return Wiki.objects.filter(is_published=True)

class ShowPost(DetailView):
    model = Wiki
    template_name = 'wiki/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = context['post']
        return context

class WikiCategory(ListView):
    model = Wiki
    template_name = 'wiki/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Категория: ' + str(context['posts'][0].cat)
        return context

    def get_queryset(self):
        return Wiki.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

def about(request):
    return render(request,'wiki/about.html', {'menu': menu, 'title': 'О сайте'})

def feedback(request):
    return render(request,'wiki/feedback.html', {'menu': menu, 'title': 'Обратная связь'})

def contacts(request):
    return render(request,'wiki/contacts.html', {'menu': menu, 'title': 'Контакты'})

def login(request):
    return render(request,'wiki/login.html', {'menu': menu, 'title': 'Войти'})


class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'wiki/addpage.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Добавить статью'
        return context

def archive(request, year):
    return HttpResponse(f"<h1>Архив по годам</h1><p>Архив за <b>{year}</b> год</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')