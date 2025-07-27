from io import BytesIO
import requests
from django.core.exceptions import ValidationError
from django.db import models
import os
from django.core.files import File


class Organizers(models.Model):
    title = models.CharField(verbose_name='Название')
    short_description = models.CharField(verbose_name='Краткое описание', max_length=500)
    long_description = models.TextField(verbose_name='Описание')
    coordinates_lng = models.FloatField(verbose_name='Долгота', null=False, blank=False)
    coordinates_lat = models.FloatField(verbose_name='Широта', null=False, blank=False)

    def __str__(self):
        return f'{self.title}'


class Image(models.Model):
    organizer = models.ForeignKey(Organizers, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(verbose_name='Изображение', upload_to='images/', blank=True, null=True)
    url = models.URLField(verbose_name='URL изображения', blank=True, null=True)

    def clean(self):
        super().clean()
        if not self.image and not self.url:
            raise ValidationError("Необходимо указать либо URL изображения, либо загрузить файл")
        if self.image and self.url:
            raise ValidationError("Можно указать только один источник изображения - либо URL, либо файл")

    def save(self, *args, **kwargs):
        if self.url and not self.image:
            response = requests.get(self.url)
            response.raise_for_status()

            file_name = os.path.basename(self.url.split("?")[0])

            self.image.save(
                file_name,
                File(BytesIO(response.content)),
                save=False
            )
        super().save(*args, **kwargs)


    def __str__(self):
        return f"Фото {self.organizer}"
