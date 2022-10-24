from django.shortcuts import render, get_object_or_404

from pypro.aperitivos.models import Video

videos = [
    Video(slug='belezadopython', titulo='Video Aperitivo: A Beleza de Python', vimeo_id='760852969'),
    Video(slug='POO', titulo='Programação Orientada a Objetos', vimeo_id='760876240'),
]

videos_dct = {v.slug: v for v in videos}


def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})


def video(request, slug):
    video = get_object_or_404(Video, slug=slug)
    return render(request, 'aperitivos/video.html', context={'video': video})
