from rest_framework import generics
from .serializers import TripSerializer
from trips.models import Trip, Activity

# Create your views here.
class AllTripsList(generics.ListAPIView):
    serializer_class = TripSerializer

    def get_queryset(self):
        return Trip.objects


# Create your views here.
class UpdateTrips(generics.UpdateAPIView):
    serializer_class = TripSerializer

    def get_queryset(self):
        return Trip.objects
