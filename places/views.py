from django.shortcuts import render
from places.models import Organizers


def start_page(request):
    organizers = Organizers.objects.all()
    features = []
    for organizer in organizers:
        place_id =+ 1
        feature = {
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [organizer.coordinates_lng, organizer.coordinates_lat]
                    },
                    "properties": {
                        "title": organizer.title,
                        "placeId": place_id,
                        "detailsUrl": "https://raw.githubusercontent.com/devmanorg/where-to-go-frontend/master/places/moscow_legends.json"
                    }
                }
        features.append(feature)
    context =  {
        "type": "FeatureCollection",
        "features": features,
    }
    data = {"context": context}
    return render(request, 'template.html', context=data)
