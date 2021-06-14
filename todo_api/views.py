from django.shortcuts import render
from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.response import Response
from rest_framework import status


class ListTodo(GenericAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def get(self, request):
        queryset = self.get_queryset().order_by('-created_at')
        serializer = TodoSerializer(queryset, many=Todo)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SingleTodo(RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
