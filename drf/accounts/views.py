from django.shortcuts import render
from crud.models import Contact
from crud.serailizer import ContactSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions
from rest_framework.authentication import BasicAuthentication,TokenAuthentication,SessionAuthentication
from django.contrib.auth.models import User
from .serializer import Userserializer
# Create your views here.

class Contacacountt(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    authentication_classes = [BasicAuthentication]


class userRegisterview(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = Userserializer
    permission_classes = [AllowAny]