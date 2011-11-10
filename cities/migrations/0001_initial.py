# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'City'
        db.create_table('cities_city', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('usgs_feature_number', self.gf('django.db.models.fields.IntegerField')()),
            ('feature', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('pop_range', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('population_2000', self.gf('django.db.models.fields.IntegerField')()),
            ('fips_5', self.gf('django.db.models.fields.IntegerField')()),
            ('county', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('county_fips', self.gf('django.db.models.fields.IntegerField')()),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('state_fips', self.gf('django.db.models.fields.IntegerField')()),
            ('display', self.gf('django.db.models.fields.IntegerField')()),
            ('point', self.gf('django.contrib.gis.db.models.fields.PointField')()),
        ))
        db.send_create_signal('cities', ['City'])


    def backwards(self, orm):
        
        # Deleting model 'City'
        db.delete_table('cities_city')


    models = {
        'cities.city': {
            'Meta': {'object_name': 'City'},
            'county': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'county_fips': ('django.db.models.fields.IntegerField', [], {}),
            'display': ('django.db.models.fields.IntegerField', [], {}),
            'feature': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'fips_5': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'point': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'pop_range': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'population_2000': ('django.db.models.fields.IntegerField', [], {}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'state_fips': ('django.db.models.fields.IntegerField', [], {}),
            'usgs_feature_number': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['cities']
