from django.shortcuts import render
from crud.models import Contact
from crud.serailizer import ContactSerializer  
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions
from rest_framework.authentication import BasicAuthentication, TokenAuthentication, SessionAuthentication
from django.contrib.auth.models import User
from .serializer import Userserializer
from .custompermission import ContactPermission
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication 
class Contacacountt(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    # authentication_classes = [JWTAuthentication]  # Use JWT authentication for this view


class userRegisterview(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = Userserializer
    permission_classes = [AllowAny]  
    http_method_names = ['post']  # Only allow POST for registration


#token authorization for login
class loginview(viewsets.ModelViewSet):
    queryset=User.objects.all()
    permission_classes = [AllowAny]  # No authentication needed for login
    authentication_classes = []  # No authentication classes needed
    
    def create(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        
        # Validate input
        if not username or not password:
            return Response(
                {'error': 'Please provide both username and password'},
                status=status.HTTP_400_BAD_REQUEST
            )
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Fixed: token = Token.objects.get_or_create(user=user) returns (token, created)
            token, created = Token.objects.get_or_create(user=user)
            
            return Response(
                {
                    'token': token.key,
                    'user_id': user.id,
                    'username': user.username,
                    'message': 'Login successful'
                },
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {'error': 'Invalid username or password'},
                status=status.HTTP_401_UNAUTHORIZED
            )