from rest_framework import generics
from .serializers import TripSerializer, ActivitySerializer
from trips.models import Trip, Activity

# Create your views here.
class AllTripsList(generics.ListAPIView):
    serializer_class = TripSerializer

    def get_queryset(self):
        return Trip.objects


class ActivitiesList(generics.ListAPIView):
    serializer_class = ActivitySerializer

    def get_queryset(self):
        parent_trip = self.kwargs["parent_trip"]
        return Activity.objects.filter(parent_trip=parent_trip)


class CreateNewTrip(generics.CreateAPIView):
    serializer_class = TripSerializer

    def perform_create(self, serializer):
        serializer.save()
