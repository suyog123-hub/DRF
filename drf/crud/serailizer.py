from .models import Contact
from rest_framework import serializers
import re
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contact
        fields="__all__"

    
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
    
    def validate_email(self,email):
        pattern = r'^[a-zA-Z0-9._%+-]+@gmail\.com$' #it will check if the email is valid and ends with @gmail.com
        if not re.match(pattern,email):
            raise serializers.ValidationError('Email must be a valid email address and end with @gmail.com')
        
        return email
