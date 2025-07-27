from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
import requests

from places.models import Organizers


def add_json_to_db(url):
    response = requests.get(url)
    response.raise_for_status()
    response_json = response.json()
    organizer, created = Organizers.objects.get_or_create(
        title=response_json['title'],
        short_description=response_json['description_short'],
        long_description=response_json['description_long'],
        defaults={'coordinates_lng': response_json['coordinates']['lng'], 'coordinates_lat': response_json['coordinates']['lat']}
    )
    for number_of_image, image_url in enumerate(response_json['imgs'], start=0):
        image_response = requests.get(image_url)
        image_response.raise_for_status()
        organizer.images.create(
            image=ContentFile(image_response.content, f'{organizer.title}_{number_of_image}.jpg'),
            ordinal_number=number_of_image
        )


class Command(BaseCommand):
    help = 'Add demo data to database'

    def handle(self, *args, **options):
        if options['url']:
            add_json_to_db(options['url'])

    def add_arguments(self, parser):
        parser.add_argument(
            'url',
            nargs='?',
            help='URL на JSON файл с данными',
        )
