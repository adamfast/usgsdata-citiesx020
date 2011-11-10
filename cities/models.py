from django.contrib.gis.db import models

class City(models.Model):
	usgs_feature_number = models.IntegerField()
	feature = models.CharField(max_length=64)
	name = models.CharField(max_length=256)
	pop_range = models.CharField(max_length=128)
	population_2000 = models.IntegerField()
	fips_5 = models.IntegerField()
	county = models.CharField(max_length=64)
	county_fips = models.IntegerField()
	state = models.CharField(max_length=2)
	state_fips = models.IntegerField()
	display = models.IntegerField()
	point = models.PointField(srid=4326)

	objects = models.GeoManager()

	def __unicode__(self):
		return u'%s, %s' % (self.name, self.state)
