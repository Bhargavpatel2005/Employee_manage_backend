from rest_framework import serializers
from .models import Employee_add,post_job,job_application,job_interview,Employee_leave,Employee_salary,Employee_performance,Employee_training,Employee_attendance

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee_add
        fields = '__all__'

class post_jobSerializer(serializers.ModelSerializer):
    class Meta:
        model = post_job
        fields = '__all__'

class job_applicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = job_application
        fields = '__all__'

class job_interviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = job_interview
        fields = '__all__'
        
class Employee_leaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee_leave
        fields = '__all__'

class Employee_salarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee_salary
        fields = '__all__'

class Employee_performanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee_performance
        fields = '__all__'  

class Employee_trainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee_training
        fields = '__all__'

class Employee_attendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee_attendance
        fields = '__all__'

class Employee_performanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee_performance
        fields = '__all__'
        
