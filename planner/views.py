from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Destination, Itinerary
from .serializers import DestinationSerializer, ItinerarySerializer, AttractionSerializer

# Destination API views
class DestinationListCreate(APIView):
    def get(self, request):
        destinations = Destination.objects.all()
        serializer = DestinationSerializer(destinations, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DestinationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Itinerary API views
class ItineraryListCreate(APIView):
    def get(self, request):
        itineraries = Itinerary.objects.all()
        serializer = ItinerarySerializer(itineraries, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ItinerarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AttractionAdd(APIView):
    def post(self, request, destination_id):
        destination = Destination.objects.get(id=destination_id)  # Fetch the destination by ID
        # Add the attraction to the specific destination
        serializer = AttractionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(destination=destination)  # Associate the attraction with the destination
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)