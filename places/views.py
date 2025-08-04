from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from places.models import Organizers


def start_page(request):
    organizers = Organizers.objects.all()
    features = []
    for organizer in organizers:
        feature = {
                    'type': 'Feature',
                    'geometry': {
                        'type': 'Point',
                        'coordinates': [organizer.coordinates_lng, organizer.coordinates_lat]
                    },
                    'properties': {
                        'title': organizer.title,
                        'placeId': organizer.id,
                        'detailsUrl': reverse('organizer', args=[organizer.id])
                    }
                }
        features.append(feature)
    context =  {
        'type': 'FeatureCollection',
        'features': features,
    }
    data = {'context': context}
    return render(request, 'template.html', context=data)


def show_place(request, id):
    organizer = get_object_or_404(Organizers,pk=id)
    images = organizer.images.all()
    urls = []

    for image in images:
        urls.append(image.image.url)
    place_dict = model_to_dict(organizer, fields=['title', 'short_description', 'long_description'])
    place_dict['coordinates'] = [organizer.coordinates_lng, organizer.coordinates_lat]
    place_dict['imgs'] = urls

    return JsonResponse(place_dict, safe=False, json_dumps_params={'ensure_ascii': False})
