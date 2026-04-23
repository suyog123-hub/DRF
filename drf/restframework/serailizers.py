from rest_framework import serializers, viewsets
from .models import Student
import re
class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()
    phone = serializers.CharField(max_length=15)
    email = serializers.EmailField()

    #it will convert the json data into a python dictionary and validate the data
    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.age=validated_data.get('age',instance.age)
        instance.phone=validated_data.get('phone',instance.phone)
        instance.email=validated_data.get('email',instance.email)
        instance.save()
        return instance


    def validate_name(self,name):
        if len(name)<2:
            raise serializers.ValidationError('Name must be at least 2 characters long')
        
        return name # else it will return the name value to the serializer and it will be saved in the database
    
    def validate_age(self,age):
        if age < 0 or age > 100:
            raise serializers.ValidationError('Age must be between 0 and 100')
        
        return age # else it will return the age value to the serializer and it will be saved in the database
    
    def validate_phone(self,phone):
        pattern = r'^\d{10}$'
        if not re.match(pattern, phone):
            raise serializers.ValidationError('Phone number must be 10 digits long and contain only numbers')
        
        return phone
    
    def validate_emial(self,email):
        pattern = r'^[a-zA-Z0-9._%+-]+@gmail\.com$' #it will check if the email is valid and ends with @gmail.com
        if not re.match(pattern,email):
            raise serializers.ValidationError('Email must be a valid email address and end with @gmail.com')
        
        return email