from rest_framework import serializers
from .models import *

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee_add
        fields = '__all__'

class post_jobSerializer(serializers.ModelSerializer):
    # job_salary = serializers.SerializerMethodField()
    class Meta:
        model = post_job 
        # fields = ['id', 'job_title', 'job_department', 'job_position', 'job_experience', 'job_type', 'job_education', 
        #           'job_skills', 'job_description','job_Responsibilities','job_location',
        #           'job_min_salary','job_max_salary','job_status', 'job_created_at','Recruitment_start_Period','Recruitment_end_Period','job_updated_at']
        fields='__all__'
    # def get_job_salary(self, obj):
    #     return {
    #         'min_salary': obj.job_min_salary,
    #         'max_salary': obj.job_max_salary
    #     }
    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #     data['job_salary'] = {
    #         'min_salary': instance.job_min_salary,
    #         'max_salary': instance.job_max_salary
    #     }
    #     data.pop('job_min_salary', None)
    #     data.pop('job_max_salary', None)
    #     return data

    # def validate(self, attrs):
    #     job_salary = self.initial_data.get('job_salary')
    #     if job_salary:
    #         attrs['job_min_salary'] = job_salary.get('min_salary')
    #         attrs['job_max_salary'] = job_salary.get('max_salary')
    #     return attrs

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
    

class hr_department_Serializer(serializers.ModelSerializer):
    skill = serializers.ListField(
        child=serializers.CharField(), write_only=True)
    # skill_display = serializers.CharField(source='skill', read_only=True)

    class Meta:
        model = HR_department
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['skill'] = instance.skill.split(',') if instance.skill else []
        return rep

    def create(self, validated_data):
        skills = validated_data.pop('skill', [])
        validated_data['skill'] = ','.join(skills)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        skills = validated_data.pop('skill', None)
        if skills is not None:
            validated_data['skill'] = ','.join(skills)
        return super().update(instance, validated_data)