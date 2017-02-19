"""djangular URL Configuration
"""

from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from restapi.views import PlacesViewIndex, PlacesFormView

urlpatterns = [
    url(r'^api/', include('restapi.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^index/$', PlacesViewIndex.as_view(), name="place_index"),
    url(r'^add-place/$', PlacesFormView.as_view(), name="place_form"),
    url(r'^$', PlacesViewIndex.as_view(), name="place_index"),
]
