from rest_framework import serializers
from .models import CarsTable, CustomUser, Favorite

class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarsTable
        fields = '__all__' 

class FavouriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'
    
    def validate_rating(self, value):
        if value < 1 or value > 10:
            raise serializers.ValidationError("Rating must be between 1 and 10")
        return value
