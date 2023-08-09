from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Menu,Booking  # Replace 'Menu' with the name of your Django model

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu  # Replace 'Menu' with the name of your Django model
        fields = '__all__'  # Use '__all__' to include all model fields in the serializer


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking  # Replace 'Menu' with the name of your Django model
        fields = '__all__'  # Use '__all__' to include all model fields in the serializer
