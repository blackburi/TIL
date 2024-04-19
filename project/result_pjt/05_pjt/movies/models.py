from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Genre(models.Model) :
    genre = models.TextField()
    def __str__(self) :
        return self.genre

class Movie(models.Model) :
    title = models.CharField(max_length=50)
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users=models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
    image = models.ImageField(blank=True, upload_to='%Y/%M/%d')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    grade = models.FloatField()


class Comment(models.Model) :
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users=models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_comments')
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
