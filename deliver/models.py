from django.db import models
from client.models import Image ,Client
status = ((0,'In progress'),(1,'In way'),(2, 'Cancel'),(3,'Delivered'))

class StatusQuerySet(models.QuerySet):

    def status_by(self,status=0):
        return self.filter(delivery_status=1)

class StatusManager(models.Manager):
    def get_queryset(self):
        return StatusQuerySet(self.model, query=self._db)

    def statusProgress(self):
        return self.get_queryset().status_by()

class Delivery(models.Model):
    title =  models.CharField(max_length=255)
    deliver_phone = models.CharField(max_length=255)
    delivery_address =  models.CharField(max_length=255)
    delivery_status = models.IntegerField(choices=status, default=0)
    show = models.BooleanField(default=1)
    geo_location = models.CharField(max_length=255,null=True)
    ip  = models.CharField(max_length=255, null=True)
    client  = models.OneToOneField(Client,on_delete=models.CASCADE)
    pictures  = models.ForeignKey(Image, on_delete=models.CASCADE)
    created =  models.DateTimeField('cretae delivery time')
    status_manager = StatusManager

    class Meta:
       pass
       verbose_name = 'Deliverie'


