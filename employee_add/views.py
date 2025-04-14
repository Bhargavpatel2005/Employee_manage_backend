from django.shortcuts import render
from rest_framework import viewsets
from .models import Employee_add
from .Serializer import EmployeeSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee_add.objects.all()
    serializer_class = EmployeeSerializer

