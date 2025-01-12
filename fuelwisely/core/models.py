from django.db import models
from django.db.models import Sum

# Emission Factors (CO₂ in grams per kilometer)
EMISSION_FACTORS = {
    'car': {'small': 135, 'average': 165, 'large': 215, 'big': 300},
    'bike': {'small': 45, 'average': 60, 'large': 85},
    'scooter': {'small': 35, 'average': 45, 'large': 60},
    'bus': {'small': 30, 'average': 40, 'large': 55},
    'train': {'electric': 20, 'diesel': 55},
}

# Transportation Model
class Transportationmodel(models.Model):
    vehicle_type = models.CharField(
        max_length=50,
        choices=[
            ('car', 'Car'),
            ('bike', 'Bike'),
            ('bus', 'Bus'),
            ('scooter', 'Scooter'),
        ]
    )
    distance = models.FloatField(help_text="Distance travelled in kilometers")
    mode = models.CharField(
        max_length=50,
        choices=[
            ('public', 'Public'),
            ('private', 'Private'),
        ]
    )
    vehicle_size = models.CharField(
        max_length=50,
        choices=[
            ('small', 'Small'),
            ('average', 'Average'),
            ('large', 'Large'),
            ('big', 'Big'),
        ],
        help_text="Size category of the vehicle"
    )
    emissions = models.FloatField(help_text="CO₂ emissions in grams", blank=True, null=True)

    def calculate_emissions(self):
        """
        Calculate emissions based on vehicle type, size, and distance.
        """
        factor = EMISSION_FACTORS.get(self.vehicle_type, {}).get(self.vehicle_size, 0)
        self.emissions = factor * self.distance

    def save(self, *args, **kwargs):
        # Automatically calculate emissions before saving
        self.calculate_emissions()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Transportation_Log: {self.vehicle_type} ({self.vehicle_size}) - {self.mode}"

# Emissions Summary Model
class EmissionsSummary(models.Model):
    total_distance = models.FloatField(default=0.0, help_text="Total distance traveled in kilometers")
    total_emissions = models.FloatField(default=0.0, help_text="Total CO₂ emissions in grams")

    def __str__(self):
        return f"Distance: {self.total_distance} km, Emissions: {self.total_emissions}"

    @classmethod
    def calculate_totals(cls):
        """
        Aggregate total distance and emissions from the Transportationmodel.
        """
        total_distance = Transportationmodel.objects.aggregate(Sum('distance'))['distance__sum'] or 0.0
        total_emissions = Transportationmodel.objects.aggregate(Sum('emissions'))['emissions__sum'] or 0.0

        summary, created = cls.objects.get_or_create(id=1)
        summary.total_distance = total_distance
        summary.total_emissions = total_emissions
        summary.save()

        return summary