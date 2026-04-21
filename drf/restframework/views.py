from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student
from .serailizers import StudentSerializer

class APITestView(APIView):
    def get(self,request):
        students = Student.objects.all() #complex data 
        serializer = StudentSerializer(students, many=True) #it will convert the queryset into a list of dictionaries
        return Response({'message':serializer.data}) #it will return the data in json format
    
    def post(self,request):
        print(request.data) #it will print the data sent by the client in the console
        serailizer = StudentSerializer(data=request.data) #it will convert the json data into a python dictionary
        if serailizer.is_valid(): 
            serailizer.save() 

            return Response({'message':'Data received successfully'})
    