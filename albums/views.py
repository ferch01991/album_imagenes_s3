from django import forms
from django.shortcuts import redirect, render

from .models import Album
from .forms import AlbumForm

from django.views.generic import DetailView
from django.views.generic import ListView

# Create your views here.

class AlbumDetailView(DetailView):
    model = Album
    template_name = 'albums/detail.html'

class AlbumListView(ListView):
    model = Album
    template_name = 'albums/list.html'
    paginate_by = 10

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['title'] = 'Galeria'
        context['form'] = AlbumForm()
        return context

def create(request):
    form = AlbumForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        album = form.save()

        return redirect('albums:list')


