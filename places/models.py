from django.db import models


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
    url = models.URLField(max_length=500)
    caption = models.CharField(max_length=200, blank=True)
    order = models.PositiveIntegerField(default=0, verbose_name='Порядок', editable=False)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"Фото {self.organizer}"
