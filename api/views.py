from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Course
from .serializers import CourseSerialziers
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
@api_view(['GET', 'POST'])
def CoursesView(request):
    if request.method == 'GET':
        course = Course.objects.all()
        serializer = CourseSerialziers(course, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = CourseSerialziers(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def CourseListView(request, pk):
    try:
        data = Course.objects.get(pk = pk)
    except Course.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = CourseSerialziers(data)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
        

    if request.method == 'PUT':
        serializer = CourseSerialziers(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'DELETE':
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
