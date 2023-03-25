from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializer import studentsSerializer
from .models import students
import io, requests
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework import serializers



class StudentApi(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            student_data = students.objects.get(id=id)  
            print('.................',student_data)
            serialized_data = studentsSerializer(student_data)
            return Response(serialized_data.data)
        
        student_data= students.objects.all()
        serialized_data = studentsSerializer(student_data, many=True)
        return Response(serialized_data.data)

    def post(self, request, format=None):
        serialized_data = studentsSerializer(data = request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response({'msg':'Data Created'},status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request,pk, format=None):
        id = pk
        get_stu = students.objects.get(pk=id)
        serialized_data = studentsSerializer(get_stu, data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response({'msg':'Complete Data updated'})
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        id = pk
        get_stu = students.objects.get(pk=id)
        serialized_data = studentsSerializer(get_stu, data=request.data, partial =True)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response({'msg':'Complete Data updated'})
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
