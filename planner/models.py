from django.db import models

class Destination(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    image = models.URLField()  # URL of the destination image
    description = models.TextField()
    local_experiences = models.TextField()
    estimated_budget = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Attraction(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name="top_attractions")
    name = models.CharField(max_length=100)
    image = models.URLField()  # URL of the attraction image
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Itinerary(models.Model):
    trip_name = models.CharField(max_length=100)
    destinations = models.ManyToManyField(Destination)  # Many destinations in one itinerary
    total_trip_duration = models.IntegerField()  # Duration in days
    estimated_budget = models.DecimalField(max_digits=10, decimal_places=2)
    daily_itinerary = models.JSONField()  # Store daily itinerary as JSON

    def __str__(self):
        return self.trip_name

class Blog(models.Model):
    country_name = models.CharField(max_length=100)
    image = models.URLField()
    short_description = models.TextField()
    article = models.TextField()

    def __str__(self):
        return self.country_name
