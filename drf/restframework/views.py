from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student
from .serailizers import StudentSerializer
from rest_framework import status
from .global_message import MESSAGE
class APITestView(APIView):
    def get(self,request):
        try:
            students = Student.objects.filter(is_delete=False) #complex data 
            serializer = StudentSerializer(students, many=True) #it will convert the queryset into a list of dictionaries

            return Response({MESSAGE:serializer.data}) #it will return the data in json format
        except Exception as e:
            return Response({MESSAGE:str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def post(self,request):
        try:
            serailizer = StudentSerializer(data=request.data) #it will convert the json data into a python dictionary
            if serailizer.is_valid(): 
                serailizer.save() 
                return Response({MESSAGE:'Data sent to database  successfully'}, status=status.HTTP_201_CREATED)
            else:
                return Response({MESSAGE:serailizer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({MESSAGE:str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def put(self,request,id):
        try:
            instance=Student.objects.get(id=id)
            serializer=StudentSerializer(instance=instance,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({MESSAGE:'Data updated successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
             return Response({MESSAGE:str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def patch(self,request,id):
        try:
            instance=Student.objects.get(id=id)
            serializer=StudentSerializer(instance=instance,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({MESSAGE:'Data updated successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
             return Response({MESSAGE:str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def delete(self,request,id):
        try:
            data=Student.objects.get(id=id)
            data.is_delete=True
            data.save()
            return Response({MESSAGE:'Data deleted successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
             return Response({MESSAGE:str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        


