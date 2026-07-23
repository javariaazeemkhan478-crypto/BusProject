from django.db import models
from django.contrib.auth.models import User
from schedules.models import Schedule

class Booking(models.Model):
    STATUS_CHOICES = [
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    schedule    = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    seat_number = models.IntegerField()
    booked_at   = models.DateTimeField(auto_now_add=True)
    status      = models.CharField(max_length=20, choices=STATUS_CHOICES, default='confirmed')

    def __str__(self):
        return f"Booking {self.id} by {self.user.username}"