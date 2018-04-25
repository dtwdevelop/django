# from django.shortcuts import render
# from django.views.decorators.csrf import csrf_exempt
from .models import Client, Image
from client.api import ClientSerializer ,ImageSealizer
from rest_framework import generics
from rest_framework import permissions
from django.shortcuts import render_to_response
import  urllib.request as url
from django.http import JsonResponse
from project.settings import gMap

def app(request):
    response = render_to_response("client.html",{});
    return response

def gmap(request):
    try:
        city =request.GET['city']
        data = ""
        # city = 'London'
        with url.urlopen('https://maps.googleapis.com/maps/api/place/autocomplete/json?input={0}&language=en&key={1}'.format(city,gMap)) as t:
           data = t.read()

        return JsonResponse(data.decode('utf-8','slashescape'),safe=False)

    except (url.HTTPError):
        pass





class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes =  (permissions.IsAuthenticatedOrReadOnly,)


class ClientDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ImagesList(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSealizer



