from django.contrib.gis import admin

from cities.models import *

class CityAdmin(admin.OSMGeoAdmin):
	list_display = ('__unicode__', 'population_2000')
	list_filter = ('pop_range',)
	search_fields = ('name',)

admin.site.register(City, CityAdmin)
