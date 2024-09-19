from rest_framework import viewsets
from books.api import serializers
from books.models import Books


class BooksViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BooksSerializer
    queryset = Books.objects.all()
