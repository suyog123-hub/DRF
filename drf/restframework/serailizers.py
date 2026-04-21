from rest_framework import serializers, viewsets
from .models import Student

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()
    phone = serializers.CharField(max_length=15)
    email = serializers.EmailField()

    #it will convert the json data into a python dictionary and validate the data
    def create(self, validated_data):
        return Student.objects.create(**validated_data)