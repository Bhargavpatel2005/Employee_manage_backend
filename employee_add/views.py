from django.shortcuts import render
from rest_framework import viewsets
from .models import Employee_add,post_job
from .Serializer import EmployeeSerializer,post_jobSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee_add.objects.all()
    serializer_class = EmployeeSerializer

class post_job(viewsets.ModelViewSet):
    queryset = post_job.objects.all()
    serializer_class = post_jobSerializer
