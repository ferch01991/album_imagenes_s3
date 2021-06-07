from django.urls import path

from .views import create, list

app_name = 'albums'
urlpatterns = [
    path('', list, name='list'),
    path('create/', create, name='create'),
]