from rest_framework import serializers
from .models import Employee_add,Login,post_job,job_application,job_interview,Employee_leave,Employee_salary,Employee_performance,Employee_training,Employee_attendance

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee_add
        fields = '__all__'

class post_jobSerializer(serializers.ModelSerializer):
    # job_salary = serializers.SerializerMethodField()
    class Meta:
        model = post_job 
        fields = ['id', 'job_title', 'job_department', 'job_position', 'job_experience', 'job_type', 'job_education', 'job_skills', 'job_description', 'job_location','job_min_salary','job_max_salary','job_status', 'job_created_at']

    def get_job_salary(self, obj):
        return {
            'min_salary': obj.job_min_salary,
            'max_salary': obj.job_max_salary
        }
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['job_salary'] = {
            'min_salary': instance.job_min_salary,
            'max_salary': instance.job_max_salary
        }
        del data['job_min_salary']
        del data['job_max_salary']
        return data

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
        
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = ['id','email', 'password']
        extra_kwargs = {'write_only': True}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    
    