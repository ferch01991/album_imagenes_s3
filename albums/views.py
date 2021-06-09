from images.forms import UploadFileForm
from django.shortcuts import redirect, render
from django.conf import settings

from .models import Album
from .forms import AlbumForm

from django.views.generic import DetailView
from django.views.generic import ListView

# Create your views here.

class AlbumDetailView(DetailView):
    model = Album
    template_name = 'albums/detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['title'] = self.get_object().title
        context['images'] = self.get_object().images
        context['form'] = UploadFileForm({
            'album_id': self.get_object().id
        })
        return context

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
        # album = form.save()
        album = Album.objects.create_by_aws(settings.BUCKET, form.cleaned_data['title'], form.cleaned_data['description'])

        return redirect('albums:list')


