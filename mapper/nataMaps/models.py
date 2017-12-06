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
    lat = models.DecimalField (max_digits=9, decimal_places=6)
    lng = models.DecimalField (max_digits=9, decimal_places=6)

class DieselPM(models.Model):
    tract = models.ForeignKey(Tract,on_delete="cascade")
    total_conc = models.DecimalField(max_digits=4,decimal_places=2)
    
