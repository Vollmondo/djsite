from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', WikiMain.as_view(), name='home'),
    path('about/', about, name='about'),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('contacts', contacts, name='contacts'),
    path('feedback', feedback, name='feedback'),
    path('login', login, name='login'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', WikiCategory.as_view(), name='category'),
    path('search/', WikiSearch.as_view(), name='search')
]