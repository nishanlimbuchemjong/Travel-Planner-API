from rest_framework import serializers
from .models import Destination, Attraction, Itinerary, Blog

class AttractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attraction
        fields = ['id', 'name', 'image', 'location']

class DestinationSerializer(serializers.ModelSerializer):
    top_attractions = AttractionSerializer(many=True, required=False) 

    class Meta:
        model = Destination
        fields = ['id', 'name', 'country', 'image', 'description', 'local_experiences', 'estimated_budget', 'top_attractions']

class ItinerarySerializer(serializers.ModelSerializer):
    destinations = serializers.PrimaryKeyRelatedField(queryset=Destination.objects.all(), many=True)

    class Meta:
        model = Itinerary
        fields = ['id', 'trip_name', 'destinations', 'total_trip_duration', 'estimated_budget', 'daily_itinerary']

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'