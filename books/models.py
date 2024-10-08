from django.db import models
from uuid import uuid4


def upload_image_book(instance, filename):
    return f'{instance.id_book}-{filename}'


class Books(models.Model):
    id_book = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    release_year = models.IntegerField()
    state = models.CharField(max_length=200)
    pages = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    publishing_company = models.CharField(max_length=200)
    image = models.ImageField(
        upload_to=upload_image_book, blank=True, null=True)

    def __str__(self):
        return f'Title: {self.title} | Author: {self.author} '
