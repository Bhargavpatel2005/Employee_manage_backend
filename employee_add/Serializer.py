from rest_framework import serializers
from .models import Employee_add

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee_add
        fields = '__all__'
