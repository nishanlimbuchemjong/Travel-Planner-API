from django.urls import path
from . import views

urlpatterns = [
    path('destinations/', views.DestinationListCreate.as_view(), name='destination-list-create'),
    path('itineraries/', views.ItineraryListCreate.as_view(), name='itinerary-list-create'),
    path('destinations/<int:destination_id>/attractions/', views.AttractionList.as_view(), name='attraction-list')
]