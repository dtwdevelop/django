from tastypie.resources import ModelResource
from .models import Client
from django.contrib.auth.models import User
from tastypie.authorization import  DjangoAuthorization
from tastypie import fields
from django.conf.urls import url
from tastypie.utils import trailing_slash

class UserResource(ModelResource):
    class Meta:
        queryset  = User.objects.all()
        resource_name = 'user'
        excludes = ['password']

class ClientResource(ModelResource):
    user = fields.OneToOneField(UserResource,'user',full=True)
    class Meta:
        queryset = Client.object.all()
        resource_name = 'client'
        # excludes  =['password']
        # allow_method = ['post']
        authorization = DjangoAuthorization()


