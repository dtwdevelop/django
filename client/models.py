from django.db import models

from django.utils import timezone
import logging
from project.settings import ROOT_URL
from django.contrib.auth.models import User

class ActiveQuerySet(models.QuerySet):
    def active(self):
        return self.filter(status=1)

    def last_join(self):
        return filter(pub_date=timezone.now())

    def last_day(self):
        return filter(status=0)

class ActiveManager(models.Manager):

   def get_queryset(self):
       return ActiveQuerySet(self.model,query=self._db)

   def active(self):
      return self.get_queryset().active()

   def new(self):
       return self.get_queryset().last_join()

   def last_day(self):
       return self.get_queryset().last_day()

account_types = ((1,'Client'), (2,'Deliver'),)


class Image(models.Model):
    title = models.CharField(max_length=255, null=True)
    url = models.URLField(null=True, max_length=255, default='http://')
    image = models.ImageField(upload_to='',null=False)

    def __str__(self):
        return self.title

    @property
    def get_url(self):
        return ROOT_URL



class Client(models.Model):
    objects = models.Manager()
    active_users = ActiveManager()
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255,null=True)
    phone_work = models.CharField(max_length=15,null=True)
    phone_home = models.CharField(max_length=15,null=True)
    address = models.CharField(max_length=255,null=True)
    collect_address = models.CharField(max_length=255,null=True)
    type_account = models.IntegerField(choices=account_types,null=True)
    status = models.IntegerField(default=1)
    created = models.DateTimeField('created',null=True)
    pub_date = models.DateTimeField('date published',null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    photo =  models.ForeignKey(Image, on_delete=models.CASCADE,null=True,verbose_name='photo')

    def __str__(self):
        return self.name

    def save(self,*args, **kwargs):
        self.pub_date  =  timezone.now()
        self.created  =  timezone.now()
        super(Client,self).save(*args,**kwargs)
