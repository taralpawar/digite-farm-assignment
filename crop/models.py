from django.db import models
from farm.models import Farm

# Create your models here.


class Crop(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    season = models.CharField(max_length=100)
    quantity = models.IntegerField()
    plant_date = models.DateField()
    growth_time = models.IntegerField()
    land_preparation = models.IntegerField()
    irrigation_period = models.IntegerField()
    fertilizer_name = models.CharField(max_length=100)
    fertilizer_quantity = models.CharField(max_length=100)
    harvest_date = models.DateField()
    prepare_date = models.DateField()

    def __str__(self):
        return self.name
