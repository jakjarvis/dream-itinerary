from django.urls import path
from . import views

urlpatterns = [
    path("trips", views.AllTripsList.as_view()),
    path("activities/<int:parent_trip>", views.ActivitiesList.as_view()),
    path("newtrip", views.CreateNewTrip.as_view()),
]
