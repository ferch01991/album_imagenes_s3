from albums.models import Album
from images.forms import UploadFileForm
from django.shortcuts import get_object_or_404, redirect

from django.conf import settings
from AWS import upload_image

from .models import Image

# Create your views here.

def create(request):
    form = UploadFileForm(request.POST, request.FILES)

    if form.is_valid():
        file = form.cleaned_data['file']

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

        """
            {
                'file': <_io.BytesIO object at 0x7f3d4e5cdca8>, 
                '_name': 'cert1.jpg', 
                'size': 229448, 
                'content_type': 'image/jpeg', 
                'charset': None, 
                'content_type_extra': {}, 
                'field_name': 'file'
            } 
        """

        return redirect('albums:detail', album.id)
