"""Defines URL patterns for manga_app."""

from django.urls import path

from . import views

app_name = 'manga_app'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all manga titles
    path('manga_titles/', views.manga_titles, name='manga_titles')
]