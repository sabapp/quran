from django.conf.urls import url
from django.urls import include

from . import views

urlpatterns = [
    url(r'^reciter/all/$', views.AllRecitersAPIView.as_view(), name='all'),
    url(r'^reciter/lastupdate/$', views.LastUpdateAPIView.as_view(), name='all'),
]
