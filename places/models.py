from django.db import models
from tinymce.models import HTMLField


class Organizers(models.Model):
    title = models.CharField(verbose_name='Название', max_length=100)
    short_description = models.TextField(verbose_name='Краткое описание', blank=True)
    long_description = HTMLField(verbose_name='Описание', blank=True)
    coordinates_lng = models.FloatField(verbose_name='Долгота')
    coordinates_lat = models.FloatField(verbose_name='Широта')


class Image(models.Model):
    organizer = models.ForeignKey(Organizers, on_delete=models.CASCADE, related_name='images', verbose_name='Организатор')
    image = models.ImageField(verbose_name='Изображение', upload_to='images/')
    ordinal_number = models.PositiveIntegerField(verbose_name='Номер по порядку', blank=True)

    class Meta:
        ordering = ['-ordinal_number']
        indexes = [
            models.Index(fields=['organizer', 'ordinal_number'])
        ]

    def __str__(self):
        return f'Фото {self.organizer}'
