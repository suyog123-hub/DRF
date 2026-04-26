from rest_framework import serializers
from .models import Details

class DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Details
        fields='__all__'


    def validate_name(self,name):
        if len(name)<3:
            raise serializers.ValidationError('Name must be at least 2 characters long')
        
        return name # else it will return the name value to the serializer and it will be saved in the database
    
    def validate_age(self,age):
        if age < 1 or age > 105:
            raise serializers.ValidationError('Age must be between 0 and 100')
