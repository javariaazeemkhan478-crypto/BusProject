from django.db import models

class Bus(models.Model):
    BUS_TYPES = [
        ('AC', 'AC'),
        ('Non-AC', 'Non-AC'),
        ('Sleeper', 'Sleeper'),
    ]
    bus_number  = models.CharField(max_length=20)
    total_seats = models.IntegerField()
    bus_type    = models.CharField(max_length=20, choices=BUS_TYPES)

    def __str__(self):
        return f"{self.bus_number} ({self.bus_type})"