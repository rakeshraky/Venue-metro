
from django.shortcuts import render, HttpResponse
from .models import FactMembers, Members
from rest_framework import viewsets, status
from .serializers import FactMembersSerializer, MembersSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
import json
import gzip
from itertools import chain
from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_protect, csrf_exempt

@csrf_exempt
def index(request):
    return render(request, template_name='index.html')

@csrf_exempt
def get_members(request):
    # lat = request.GET['lat']
    # lng = request.GET['lng']
    lat = "-33.9286"
    lng = "150.9180"
    # queryset = Members.objects.filter().all()[0:100]
    queryset = Members.objects.raw("select top 10* from Members a inner join Australianpostcodes b on a.postal_code = b.Postcode where b.Type = 'Polygon'")
    postcodes = {}
    for i in queryset:
        i.latitude = eval(i.GeoPoint)[0]
        i.longitude = eval(i.GeoPoint)[1]
        coords = []
        for j in eval(i.Coordinates):
            for k in j:
                if len(k) <= 2:
                    coords.append(
                        {"lng": k[0], "lat": k[1]}
                    )
                else:
                    for m in k:
                        coords.append(
                            {"lng": m[0], "lat": m[1]}
                        )
        postcodes[i.postal_code] = {"coords": coords, "color": "blue", "postcode": i.postal_code}
    qs_json = serializers.serialize('json', queryset)
    # query = "SELECT * FROM Members a WHERE (acos(sin(a.latitude * 0.0175) * sin(%s * 0.0175) + cos(a.latitude * 0.0175) * cos(%s * 0.0175) * cos((%s * 0.0175) - (a.longitude * 0.0175))) * 3959 <= 62)" % (lat, lat, lng)
    # queryset2 = Members.objects.raw(query)
    return JsonResponse({'data': qs_json, 'count': 10, 'postcodes': postcodes})


   





