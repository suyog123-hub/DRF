from rest_framework import viewsets
from .models import Contact
from .serailizer import ContactSerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer