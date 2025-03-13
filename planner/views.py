from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Destination, Itinerary, Attraction
from .serializers import DestinationSerializer, ItinerarySerializer, AttractionSerializer
from django.http import JsonResponse

# Destination API views
class DestinationListCreate(APIView):
    def get(self, request):
        destinations = Destination.objects.all()
        serializer = DestinationSerializer(destinations, many=True)
        return JsonResponse(serializer.data, safe=False)


# Itinerary API views
class ItineraryListCreate(APIView):
    def get(self, request):
        itineraries = Itinerary.objects.all()
        serializer = ItinerarySerializer(itineraries, many=True)
        return JsonResponse(serializer.data, safe=False)

class AttractionList(APIView):
    def get(self, request, destination_id):
        try:
            destination = Destination.objects.get(id=destination_id)  # Fetch the destination by ID
            attractions = Attraction.objects.filter(destination=destination)  # Get attractions for the destination
            serializer = AttractionSerializer(attractions, many=True)
            return JsonResponse(serializer.data, safe=False)  # Return the attractions in JSON format
        except Destination.DoesNotExist:
            return JsonResponse({"error": "Destination not found"}, status=404)