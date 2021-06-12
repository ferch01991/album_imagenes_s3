from albums.models import Album
from .forms import UploadFileForm
from django.shortcuts import get_object_or_404, redirect, render

from .models import Image
from django.conf import settings

from AWS import upload_image


# Create your views here.

def create(request):
    form = UploadFileForm(request.POST, request.FILES)

    if form.is_valid():
        file = form.cleaned_data['file']
        print(form.cleaned_data['album_id'])

        album = get_object_or_404(Album, id=form.cleaned_data['album_id'])

        key = album.key + file._name

        if upload_image(settings.BUCKET, key, file):
            image = Image.objects.create(
                name=file._name,
                content_type = file.content_type,
                size = file.size,
                bucket=settings.BUCKET,
                key=key,
                album=album
            )

        return redirect('albums:detail', album.id)
