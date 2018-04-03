from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Client
from .models import  Image
from rest_framework.response import Response,Serializer
from django.core import serializers

class ClientInline(admin.StackedInline):
    model = Client
    can_delete = False
    exclude = ['pub_date','created']
    # fields = [('name,username'),'phone_work']
    readonly_fields = ['created']

class UserAdmin(BaseUserAdmin):
     list_filter = ['email']
     search_fields = ['name','email']
     inlines = [ClientInline]



class ImageAdmin(admin.ModelAdmin):
    def photo(self, obj):
          if (obj.image != ""):
              return '<img width="150" src="{url}images/{image}"/>'.format(url=obj.get_url,image=obj.image)
          else:
              return '<span>No image</span>'.format(obj.image)

    def hide_photo(self, request, queryset):
        pass



    hide_photo.shor_description= 'Hide Photo'

    photo.short_description = 'Photo'
    photo.allow_tags = True
    list_display = ('title', 'url', 'photo')
    actions = [hide_photo]

admin.site.unregister(User)
admin.site.register(User,UserAdmin)
admin.site.register(Image,ImageAdmin)
