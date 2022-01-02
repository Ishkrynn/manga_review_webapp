from django.db import models
from django.db.models.deletion import CASCADE

class MangaTitle(models.Model):
    """The title of a manga"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text

class Review(models.Model):
    """A review for a specific manga"""
    manga_title = models.ForeignKey(MangaTitle, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text