# from django.shortcuts import render
# from django.views.decorators.csrf import csrf_exempt
from .models import Client, Image
from client.api import ClientSerializer ,ImageSealizer
from rest_framework import generics
from rest_framework import permissions

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



