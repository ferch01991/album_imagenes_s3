from django import forms
from django.shortcuts import redirect, render

from .models import Album
from .forms import AlbumForm

# Create your views here.

def create(request):
    form = AlbumForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        album = form.save()

        return redirect('albums:list')

def list(request):
    form = AlbumForm()
    albums = Album.objects.all()
    context = {
        'title': 'Galería',
        'form': form,
        'albums': albums
    }
    return render(request, 'albums/list.html', context)
