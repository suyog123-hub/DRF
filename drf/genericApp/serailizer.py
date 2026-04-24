from rest_framework import serializers
from restframework.models import Student

class genericserializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'