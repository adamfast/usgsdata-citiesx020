A simple implementation of the U.S. National Atlas Cities and Towns of the United States database.

Data available from http://coastalmap.marine.usgs.gov/GISdata/basemaps/usa/cities/citiesx020.htm

Data is public domain. See dataset webpage for more specific information on licensing.

Installation:
	Add 'cities' to INSTALLED_APPS after putting the package on your PYTHONPATH.
	Run a syncdb or migrate (South migrations are included, and recommended)

Importing:
	manage.py city_import --path=/path/to/shapefile/
