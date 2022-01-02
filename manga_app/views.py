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

def manga_title(request, manga_id):
    """Shows a single manga and its review"""
    manga_title = MangaTitle.objects.get(id=manga_id)
    reviews = manga_title.review_set.order_by('-date_added')
    context = {'manga': manga_title, 'reviews': reviews}
    return render(request, 'manga_app/manga_title.html', context)