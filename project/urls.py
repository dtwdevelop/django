"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url ,include
from django.conf.urls.static import static
from django.contrib import admin
from client.views import ClientList,  ClientDetails ,ImagesList, app ,gmap
from rest_framework.urlpatterns import format_suffix_patterns
from .settings import MEDIA_ROOT,MEDIA_URL
from django.conf import settings





urlpatterns = [
    url(r'^$', app),
    url(r'^client/$',ClientList.as_view(),name='client'),
    url(r'^client/(?P<pk>[0-9]+)/$',ClientDetails.as_view()),
    url(r'photos/',ImagesList.as_view(),name='image'),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^map/',gmap)

]
urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

