from django.db import models

# These are data classes i.e consider them database schemas or different tables


class Trip(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    dates = models.CharField(max_length=50, blank=True)
    splash_image = models.ImageField(upload_to="trips/images/", blank=True)
    thumbnail_image = models.ImageField(upload_to="trips/images/", blank=True)

    def __str__(self):
        return self.title


class Activity(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    dates = models.CharField(max_length=50, blank=True)
    parent_trip = models.CharField(max_length=200, blank=True)
    thumbnail_image = models.ImageField(upload_to="trips/images/", blank=True)

    def __str__(self):
        return self.title
