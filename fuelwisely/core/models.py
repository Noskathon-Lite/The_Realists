from django.db import models
from django.db.models import Sum
# Create your models here.
class  Transportationmodel(models.Model):
    vehicle_type = models.CharField(max_length=50,choices=
                                       [
                                        ('car','Car'),
                                        ('bike','Bike'),
                                        ('bus','Bus'),
                                        ('scooter','Scooter'),
                                       ]
                                    )
    distance = models.FloatField(help_text = "Distance travelled in kilomeeters" )

    mode = models.CharField(max_length=50, choices=
                            [
                                ('public','Public'),
                                ('private','Private'),
                            ]
                            )
    vehicle_size = models.CharField(max_length=50, choices=[
        ('small', 'Small'),
        ('average', 'Average'),
        ('large', 'Large'),
        ('big', 'Big'),
    ], help_text ="Size category of the vehicle")
    emissions = models.FloatField(help_text = "Co2 emmissions in grams ")

    def __str__(self):
       return f"Transportation_Log:{self.vehicle_type} ({self.vehicle_size}) - {self.mode}"



class EmissionsSummary(models.Model):
    total_distance  = models.FloatField(default=0.0, help_text = "total distance traveled in kilomeeters")
    total_emissions = models.FloatField(default=0.0,help_text = "total co2 emissions ")

    def __str__(self):
        return f"Distance :{self.total_distance} km , Emissions : {self.total_emissions}" 

    @classmethod
    def calculate_totals(cls):
        
        total_distance  =  Transportationmodel.objects.aggregate(Sum('distance'))['distance__sum'] or 0.0
        total_emissions = Transportationmodel.objects.aggregate(Sum('emissions'))['emissions__sum'] or 0.0

                
        summary, created = cls.objects.get_or_create(id=1)
        summary.total_distance = total_distance
        summary.total_emissions = total_emissions
        summary.save()

        return summary