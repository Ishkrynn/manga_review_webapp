from django.contrib import admin

from manga_app.models import MangaTitle, Review

admin.site.register(MangaTitle)
admin.site.register(Review)