from django.db import models
from routes.models import Route
from buses.models import Bus

class Schedule(models.Model):
    route          = models.ForeignKey(Route, on_delete=models.CASCADE)
    bus            = models.ForeignKey(Bus, on_delete=models.CASCADE)
    departure_time = models.DateTimeField()
    arrival_time   = models.DateTimeField()
    fare           = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.route} at {self.departure_time}"

    def available_seats(self):
        booked = self.booking_set.filter(status='confirmed').count()
        return self.bus.total_seats - booked