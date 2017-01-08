from django.conf.urls import url
from views import PlaceListView, PlaceAddView, PlaceDetail, PlacesViewIndex

urlpatterns = [
    url(r'^places/$', PlaceListView.as_view(), name='place_list'),
    url(r'^places/(?P<pk>\d+)/$', PlaceDetail.as_view(), name='place_detail'),
    url(r'^places/add/$', PlaceAddView.as_view(), name='place_add'),
]
