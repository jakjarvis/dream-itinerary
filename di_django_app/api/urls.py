from django.urls import path
from . import views

urlpatterns = [
    path("trips", views.AllTripsList.as_view()),
]
