from django.db import models


class Organizers(models.Model):
    title = models.CharField(verbose_name='Название')
    image = models.URLField(max_length=500)
    short_description = models.CharField(verbose_name='Краткое описание', max_length=100)
    long_description = models.TextField(verbose_name='Описание')
    coordinates_lng = models.FloatField(verbose_name='Долгота', null=False, blank=False)
    coordinates_lat = models.FloatField(verbose_name='Широта', null=False, blank=False)

    def __str__(self):
        return f'{self.title}'
