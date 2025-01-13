from django.contrib import admin
from .models import Transportationmodel, EmissionsSummary

@admin.register(Transportationmodel)
class TransportationAdmin(admin.ModelAdmin):
    list_display = ['vehicle_type', 'distance', 'mode', 'vehicle_size', 'emissions']
    readonly_fields = ['emissions']

@admin.register(EmissionsSummary)
class EmissionsSummaryAdmin(admin.ModelAdmin):
    list_display = ['get_total_distance', 'get_total_emissions']
    readonly_fields = ['get_total_distance', 'get_total_emissions']

    def get_total_distance(self, obj):
        return obj.total_distance
    get_total_distance.short_description = 'Total Distance'

    def get_total_emissions(self, obj):
        return obj.total_emissions
    get_total_emissions.short_description = 'Total Emissions'
