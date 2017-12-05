from django.db import models

# Create your models here.

class Tract(models.Model):
    stateFP = models.IntegerField()
    stateName = models.CharField(max_length=16,null=True)
    countyFP = models.IntegerField()
    countyName = models.CharField(max_length=32,null=True)
    geoid = models.CharField(max_length=11)
    population = models.IntegerField(null=True)

class TractPoint(models.Model):
    tract = models.ForeignKey(Tract,on_delete="cascade")
    lat = models.DecimalField (max_digits=10, decimal_places=3)
    lng = models.DecimalField (max_digits=10, decimal_places=3)

class DieselPM(models.Model):
    tract = models.ForeignKey(Tract,on_delete="cascade")
    total_conc = models.DecimalField(max_digits=7,decimal_places=1)
    
