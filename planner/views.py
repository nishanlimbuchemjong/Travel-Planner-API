from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Destination, Itinerary, Attraction, Blog
from .serializers import DestinationSerializer, ItinerarySerializer, AttractionSerializer, BlogSerializer
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
        
class BlogListCreate(APIView):
    def get(self, request):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return JsonResponse(serializer.data, safe=False)

class BlogDetail(APIView):
    def get(self, request, blog_id):
        try:
            blog = Blog.objects.get(id=blog_id)
            serializer = BlogSerializer(blog)
            return JsonResponse(serializer.data, safe=False)
        except Blog.DoesNotExist:
            return JsonResponse({'error': 'Blog not found'}, status=404)