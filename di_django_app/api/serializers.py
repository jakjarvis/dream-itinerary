from rest_framework import serializers
from trips.models import Trip, Activity


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ["title", "description", "dates", "splash_image", "thumbnail_image"]


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ["title", "description", "dates", "parent_trip", "thumbnail_image"]
