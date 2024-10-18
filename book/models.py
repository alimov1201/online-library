from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Book(models.Model):
    image = models.ImageField(upload_to='book_image/')
    title = models.CharField(max_length=221)
    description = models.TextField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    views = models.PositiveIntegerField()
    file = models.FileField(upload_to='book_file/', blank=True)
    users = models.ManyToManyField(to=User)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
