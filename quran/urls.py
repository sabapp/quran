from django.conf.urls import url
from django.urls import include

from . import views

urlpatterns = [
    url(r'^reciter/all/$', views.GetAllRecitersAPIView.as_view(), name='all'),
    url(r'^reciter/lastupdate/$', views.ReciterLastUpdateAPIView.as_view()),

    url(r'^taftar/all/$', views.GetAllTafTarTextAPIView.as_view(), name='all'),
    url(r'^taftar/lastupdate/$', views.TafTarLastUpdateAPIView.as_view(), name='all'),

]
