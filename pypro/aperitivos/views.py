from django.shortcuts import render

def video(request, slug):
    videos = {
        'belezadopython' : {'titulo': 'Video Aperitivo: A Beleza de Python', 'vimeo_id': 760852969},
        'POO' : {'titulo': 'Programação Orientada a Objetos', 'vimeo_id': 760876240},
    }
    video = videos[slug]
    return render(request,'aperitivos/video.html', context={'video': video})
