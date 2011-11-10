import os
from optparse import make_option

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.contrib.gis.utils import LayerMapping

from cities.models import *

def city_import(path='/root/'):
    city_mapping = {
        'usgs_feature_number': 'CITIESX020',
        'feature': 'FEATURE',
        'name': 'NAME',
        'pop_range': 'POP_RANGE',
        'population_2000': 'POP_2000',
        'fips_5': 'FIPS55',
        'county': 'COUNTY',
        'county_fips': 'FIPS',
        'state': 'STATE',
        'state_fips': 'STATE_FIPS',
        'display': 'DISPLAY',
        'point': 'POINT',
    }
    city_shp = os.path.join(path, 'citiesx020.shp')
    lm = LayerMapping(City, city_shp, city_mapping, source_srs=4326)
    lm.save(verbose=True)


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--path', default='', dest='path',
            help='The directory where citiesx020.shp is stored.'),
    )
    help = ("Imports data from the U.S. National Atlas Cities and Towns of the United States data download.")

    def handle(self, *args, **options):
        if settings.DEBUG:
            print('You really should turn settings.DEBUG off, or else this script will eat a very large amount of your RAM.')
        else:
            input_path = options['path']

            city_import(input_path)
