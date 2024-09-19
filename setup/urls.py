
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from books.api.viewsets import BooksViewSet
from django.conf import settings
from django.conf.urls.static import static

route = routers.DefaultRouter()

route.register(r'books', BooksViewSet, basename='Books')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
