'''
views in drf:
function based view --> simple api
APIView ---> more  to mid level api 
Generic api view + mixin  --> used to reuse the crud pattern 
concrete genric api view ---> create the crud project quickly 

viewset / model view --> high level api view which will automatically create the crud operations for us based on the model we provide
'''
from rest_framework.generics import ListAPIView,ListCreateAPIView,UpdateAPIView,RetrieveAPIView
from restframework.models import Student
from .serailizer import genericserializer


class Genericview(ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=genericserializer

class Genericview1(UpdateAPIView):
    queryset=Student.objects.all()
    serializer_class=genericserializer
