from nataMaps.models import *

from rest_framework import serializers

class PolygonSerializer(serializers.ModelSerializer):
    class Meta:
        model = TractPoint
        fields = ['lat','lng']

class DieselPMSerializer(serializers.ModelSerializer):
    class Meta:
        model= DieselPM
        fields = ['total_conc']
        
class DieselSerializer(serializers.ModelSerializer):
    polygon = PolygonSerializer(source='tractpoint_set',many=True)
    diesel_conc = DieselPMSerializer(source='dieselpm_set',many=True)
    
    class Meta:
        model = Tract
        fields = ['id','countyFP','stateFP','geoid','polygon','diesel_conc']

class CountiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tract
        fields = ['countyFP','countyName']
        
class StatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tract
        fields = ['stateFP','stateName']
