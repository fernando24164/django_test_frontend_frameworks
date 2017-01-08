from django.http import HttpResponse, JsonResponse
from django.views import View as ViewDjango
from django.shortcuts import render
from .models import Place
from .api.serializers import PlaceSerializer
from rest_framework import generics, permissions
from rest_framework.views import APIView, View
from rest_framework.response import Response


class PlaceListView(generics.ListAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    permission_classes = [permissions.AllowAny]


class PlaceDetail(generics.RetrieveAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    permission_classes = [permissions.AllowAny]


# Auxiliar methods just for more especific cases
class PlaceDetailView(View):
    permission_classes = [permissions.AllowAny]

    def get(self, request, pk):
        queryset = Place.objects.get(pk=pk)
        serializer = PlaceSerializer(queryset)
        return JsonResponse(serializer.data)


class PlaceAddView(APIView):
    queryset = None
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        lat = request.data.get("lat", "")
        longi = request.data.get("longi", "")
        name = request.data.get("name", "")
        cond = lat != "" and longi != "" and name != ""
        if cond:
            Place.objects.create(name=name, longi=longi, lat=lat)

        return Response(HttpResponse.status_code)


class PlacesViewIndex(ViewDjango):
    template_name = "index.html"

    def get(self, request, *args, **kargs):
        return render(request, self.template_name)
