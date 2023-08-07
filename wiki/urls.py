from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('cats/<slug:cat>/', categories, name='cats'),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive),
    path('addpage/', addpage, name='add_page'),
    path('contacts', contacts, name='contacts'),
    path('login', login, name='login'),
    path('post/<int:post_id>/', show_post, name='post'),
    path('category/<int:cat_id>/', show_category, name='category'),

]