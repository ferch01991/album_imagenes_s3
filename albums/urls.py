from django.urls import path

from .views import create, index

urlpatterns = [
    path('', index, name='list'),
    path('create/', create, name='create'),
]