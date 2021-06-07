from django import forms
from django.shortcuts import redirect, render

from .forms import AlbumForm

# Create your views here.

def create(request):
    form = AlbumForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        album = form.save()

        return redirect('albums:list')

def index(request):

    form = AlbumForm()
    context = {
        'title': 'Galería',
        'form': form
    }
    return render(request, 'albums/list.html', context)
