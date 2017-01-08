from django.contrib import admin
from models import Place, Cluster, Beacon


class PlaceAdmin(admin.ModelAdmin):
    pass


class ClusterAdmin(admin.ModelAdmin):
    pass


class BeaconAdmin(admin.ModelAdmin):
    pass

admin.site.register(Place, PlaceAdmin)
admin.site.register(Cluster, ClusterAdmin)
admin.site.register(Beacon, BeaconAdmin)
