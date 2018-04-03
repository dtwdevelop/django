# from django.shortcuts import render
# from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import  Response
from  rest_framework import status
from rest_framework.decorators import api_view
from django.http import Http404
from rest_framework.views import APIView
from .models import Client
from django.utils import timezone
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from client.api import ClientSerializer
from django.contrib.auth.models import User
from rest_framework import generics

class ClientList(APIView):

     def get(self,request,format=None):
         clients = Client.objects.all()
         seliazer = ClientSerializer(clients, many=True)
         return Response(seliazer.data)

     def post(self,request,format=None):
         serializer = ClientSerializer(data=request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data, status=status.HTTP_201_CREATED)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClientDetails(APIView):

    def get_pk(self,pk):
        try:
            client = Client.objects.get(pk=pk)
            return client
        except Client.DoesNotExist:
            raise Http404

    def get(self,request,client_id ,format=None):
        try:
            client = self.get_pk(client_id)
            serializer = ClientSerializer(client)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUES)

    def put(self,request,client_id ,format=None):
        client = self.get_pk(client_id)
        serializer = ClientSerializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,client_id ,format=None):
        client = self.get_pk(client_id)
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
