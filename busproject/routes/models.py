from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Route(models.Model):
    from_city   = models.ForeignKey(City, on_delete=models.CASCADE, related_name='departures')
    to_city     = models.ForeignKey(City, on_delete=models.CASCADE, related_name='arrivals')
    distance_km = models.IntegerField()

    def __str__(self):
        return f"{self.from_city} → {self.to_city}"