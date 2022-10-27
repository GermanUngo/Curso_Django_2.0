from django.db import models
from django.urls import reverse


class Video(models.Model):
    slug = models.CharField(max_length=50)
    titulo = models.CharField(max_length=50)
    vimeo_id = models.CharField(max_length=50)
    creation = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('aperitivos:video', args=(self.slug,))