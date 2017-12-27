A simple implementation of the U.S. National Atlas Cities and Towns of the United States database.

Data available from https://pubs.usgs.gov/of/2003/of03-001/data/basemaps/usa/cities/cities_dtl.htm

Data is public domain. See dataset webpage for more specific information on licensing.

Installation:
	Add 'cities' to INSTALLED_APPS after putting the package on your PYTHONPATH.
	Run a syncdb or migrate (South migrations are included, and recommended)

Importing:
	manage.py city_import --path=/path/to/shapefile/
