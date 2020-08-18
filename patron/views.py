
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

def index(request):
    return render(request, template_name='index.html')

def get_members(request):
    # lat = request.GET['lat']
    # lng = request.GET['lng']
    lat = "-33.9286"
    lng = "150.9180"
    # queryset = Members.objects.filter().all()[0:100]
    queryset = Members.objects.raw("SELECT * FROM Members WHERE Latitude IS NOT NULL AND Longitude IS NOT NULL")
    qs_json = serializers.serialize('json', queryset)
    query = "SELECT * FROM Members a WHERE (acos(sin(a.latitude * 0.0175) * sin(%s * 0.0175) + cos(a.latitude * 0.0175) * cos(%s * 0.0175) * cos((%s * 0.0175) - (a.longitude * 0.0175))) * 3959 <= 62)" % (lat, lat, lng)
    queryset2 = Members.objects.raw(query)
    return JsonResponse({'data': qs_json, 'count': len(queryset2)})


   





