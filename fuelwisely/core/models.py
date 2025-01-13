from django.db import models
from django.db.models import Sum

# Emission Factors (CO₂ in grams per kilometer)
EMISSION_FACTORS = {
    'car': {'small': 135, 'average': 165, 'large': 215, 'big': 300},
    'bike': {'small': 45, 'average': 60, 'large': 85},
    'scooter': {'small': 35, 'average': 45, 'large': 60},
    'bus': {'small': 30, 'average': 40, 'large': 55},
}

# Transportation Model
class Transportationmodel(models.Model):
    # Define choices as class attributes
    VEHICLE_CHOICES = [
        ('car', 'Car'),
        ('bike', 'Bike'),
        ('bus', 'Bus'),
        ('scooter', 'Scooter'),
    ]
    
    MODE_CHOICES = [
        ('public', 'Public'),
        ('private', 'Private'),
    ]
    
    SIZE_CHOICES = [
        ('small', 'Small'),
        ('average', 'Average'),
        ('large', 'Large'),
        ('big', 'Big'),
    ]

    # Model fields
    vehicle_type = models.CharField(max_length=50, choices=VEHICLE_CHOICES)
    distance = models.FloatField(help_text="Distance travelled in kilometers")
    mode = models.CharField(max_length=50, choices=MODE_CHOICES)
    vehicle_size = models.CharField(max_length=50, choices=SIZE_CHOICES)
    emissions = models.FloatField(help_text="CO₂ emissions in grams", blank=True, null=True)

    def calculate_emissions(self):
        """
        Calculate emissions based on vehicle type, size, distance, and mode (public/private).
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
    total_emissions = models.FloatField(default=0)
    average_emissions = models.FloatField(default=0)

    @classmethod
    def calculate_totals(cls):
        # Get or create the summary instance
        summary, created = cls.objects.get_or_create(id=1)
        
        # Calculate totals from all transportation records
        transportation_records = Transportationmodel.objects.all()
        total = sum(record.emissions for record in transportation_records)
        count = transportation_records.count()
        
        # Update the summary
        summary.total_emissions = total
        summary.average_emissions = total / count if count > 0 else 0
        summary.save()