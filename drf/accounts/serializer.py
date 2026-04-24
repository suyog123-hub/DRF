from rest_framework import serializers
from django.contrib.auth.models import User

class Userserializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password','password1']
       

    def validate(self,data):
        if data['password'] != data['password1']:
            raise serializers.ValidationError('Password and Confirm Password do not match')
        return data
    
    def create(self, validated_data):
        validated_data.pop('password1') # remove password1 from validated_data because it is not a field in the User model
        return User.objects.create_user(**validated_data) # create_user is a method that creates a user and hashes the password automatically)
    