from django.shortcuts import render

from .models import MangaTitle

def index(request):
    """The home page for the Manga Review Webapp"""
    return render(request, 'manga_app/index.html')

def manga_titles(request):
    """Shows all manga titles"""
    manga_titles = MangaTitle.objects.order_by('date_added')
    context = {'manga_titles': manga_titles}
    return render(request, 'manga_app/manga_titles.html', context)