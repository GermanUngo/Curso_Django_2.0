from django.test import TestCase
import pytest
from django.urls import reverse
from pypro.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('aperitivos:indice'))


def test_status_code(resp):
    assert resp.status_code == 200


@pytest.mark.parametrize(
    'titulo',
    [
        'Video Aperitivo: A Beleza de Python',
        'Programação Orientada a Objetos'
    ]
)
def test_titulo_video(resp, titulo):
    assert_contains(resp, titulo)

@pytest.mark.parametrize(
    'slug',
    [
        'belezadopython',
        'POO'
    ]
)
def test_link_video(resp, slug):
    video_link = reverse('aperitivos:video', args=(slug,))
    assert_contains(resp, f'href="{video_link}"')
