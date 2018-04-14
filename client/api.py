from rest_framework import serializers
from .models import Client, Image
from django.contrib.auth.models import User
from django.utils import timezone
import logging
from django.contrib.auth.hashers import make_password
logger = logging.getLogger(__name__)
logging.basicConfig(
    level = logging.DEBUG,
    format = '%(name)s %(levelname)s %(message)s',
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ('name,email',)
        exclude = ('groups', 'user_permissions', 'is_staff','last_login','is_active','is_superuser')

class ClientSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Client
        fields =('user','id','name','username','phone_work','phone_home',
             'address','collect_address','type_account','status','created','pub_date')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_data["password"] = make_password(user_data["password"])
        logger.info(user_data)
        user = User.objects.create(**user_data)
        client = Client.objects.create(user=user, **validated_data)
        return client
    """"
    "last_login": "2017-11-24T10:40:22Z",
            "is_superuser": false,
            "username": "admin2",
            "first_name": "client 1",
            "last_name": "lastname",
            "email": "cleint@demo2.com",
            "is_active": true,
            "date_joined"
    """
    def update(self, instance, validated_data):
        user = validated_data.pop('user')
        users = instance.user
        users.username  = user.get('username',users.username)
        users.first_name = user.get('first_name', users.first_name)
        users.last_name = user.get('last_name', users.last_name)
        users.email = user.get('email', users.email)

        instance.id  = validated_data.get('id',instance.id)
        instance.id = validated_data.get('id', instance.id)
        instance.name  =  validated_data.get('name', instance.name)
        instance.username = validated_data.get('username', instance.username)
        instance.phone_work = validated_data.get('phone_work', instance.phone_work)
        instance.phone_home = validated_data.get('phone_home', instance.phone_home)
        instance.phone_address = validated_data.get('phone_home', instance.address)
        instance.collect_address = validated_data.get('collect_address', instance.collect_address)
        instance.type_account = validated_data.get('type_account', instance.type_account)
        instance.status = validated_data.get('status', instance.status)
        instance.created = validated_data.get('created', instance.created)
        instance.pub_date = validated_data.get('pub_date', instance.pub_date)
        instance.save()
        users.save()

        return instance

class ImageSealizer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id','title','url','image')






