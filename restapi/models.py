from __future__ import unicode_literals
from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    longi = models.DecimalField(max_digits=9, decimal_places=6)


class Cluster(models.Model):
    name = models.CharField(max_length=50)
    place = models.ForeignKey(Place)


class Beacon(models.Model):
    name = models.CharField(max_length=50)
    cluster = models.ForeignKey(Cluster)
