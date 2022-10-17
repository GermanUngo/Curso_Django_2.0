from django.shortcuts import render

videos = [
    {'slug': 'belezadopython', 'titulo': 'Video Aperitivo: A Beleza de Python', 'vimeo_id': 760852969},
    {'slug': 'POO', 'titulo': 'Programação Orientada a Objetos', 'vimeo_id': 760876240},
]

videos_dct = {dct['slug']: dct for dct in videos}


def indice(request):
    return render(request,'aperitivos/indice.html', context={'videos': videos})


def video(request, slug):
    video = videos_dct[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
