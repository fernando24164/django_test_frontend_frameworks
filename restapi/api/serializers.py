from rest_framework import serializers
from ..models import Place, Cluster, Beacon


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ('name', 'lat', 'longi')


class ClusterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cluster
        fields = ('name', 'place')


class BeaconSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beacon
        fields = ('name', 'cluster')
