from rest_framework import viewsets
from rest_framework import permissions
from books.api import serializers
from books.models import Books


class BooksViewSet(viewsets.ModelViewSet):

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.BooksSerializer
    queryset = Books.objects.all()
