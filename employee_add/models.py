from django.db import models
from .choices import *
from multiselectfield import MultiSelectField

class Employee_add(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    Date_of_Birth = models.DateField(null=True, blank=True)
    Gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    Address = models.TextField()

    Job_title = models.CharField(max_length=50)
    Department = models.CharField(max_length=50)
    Employee_type = models.CharField(max_length=10, choices=JOB_TYPE)
    Salary = models.DecimalField(max_digits=10, decimal_places=2)
    Date_hired = models.DateField()

    profile_picture = models.ImageField(upload_to='employee_pics/', blank=True, null=True)
    resume = models.FileField(upload_to='resume/', blank=True, null=True)

    is_active = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.Job_title}"


class post_job(models.Model):
    job_title = models.CharField(max_length=50)
    job_department = models.CharField(max_length=50)
    job_position = models.CharField(max_length=50)
    job_experience = models.IntegerField()
    job_type = models.CharField(max_length=10)
    job_education = models.CharField(max_length=50)
    job_skills = MultiSelectField(max_length=50)
    job_description = models.TextField(max_length=1000)
    job_location = models.CharField(max_length=50)
    job_salary = models.DecimalField(max_digits=10, decimal_places=2)
    job_status = models.CharField(max_length=10)
    job_created_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.job_title

class job_application(models.Model):
    job = models.ForeignKey(post_job, on_delete=models.CASCADE)
    applicant = models.ForeignKey(Employee_add, on_delete=models.CASCADE)
    application_date = models.DateField(auto_now_add=True)
    application_status = models.CharField(max_length=10, choices=APPLICATION_STATUS)
    
    def __str__(self):
        return f"{self.applicant.first_name} {self.applicant.last_name} - {self.job.job_title}" 

class job_interview(models.Model):
    application = models.ForeignKey(job_application, on_delete=models.CASCADE)
    interview_date = models.DateField()
    interview_time = models.TimeField()
    interview_location = models.CharField(max_length=50)  
    interview_feedback = models.TextField()
    interview_result = models.CharField(max_length=10, choices=INTERVIEW_RESULT)

    def __str__(self):
        return f"{self.application.applicant.first_name} {self.application.applicant.last_name} - {self.application.job.job_title}"
    
class Employee_leave(models.Model):
    employee = models.ForeignKey(Employee_add, on_delete=models.CASCADE)
    leave_date = models.DateField()
    leave_type = models.CharField(max_length=10, choices=LEAVE_TYPE)
    leave_status = models.CharField(max_length=10, choices=LEAVE_STATUS)

    def __str__(self):
        return f"{self.employee.first_name} {self.employee.last_name} - {self.leave_date}"
    
class Employee_salary(models.Model):
    employee = models.ForeignKey(Employee_add, on_delete=models.CASCADE)
    salary_date = models.DateField()
    salary_amount = models.DecimalField(max_digits=10, decimal_places=2)   
    salary_status = models.CharField(max_length=10, choices=SALARY_STATUS)

    def __str__(self):
        return f"{self.employee.first_name} {self.employee.last_name} - {self.salary_date}"
    
class Employee_performance(models.Model):
    employee = models.ForeignKey(Employee_add, on_delete=models.CASCADE)
    performance_date = models.DateField()
    performance_rating = models.CharField(max_length=10, choices=PERFORMANCE_RATING)
    performance_feedback = models.TextField()

    def __str__(self):
        return f"{self.employee.first_name} {self.employee.last_name} - {self.performance_date}"    

class Employee_training(models.Model):
    employee = models.ForeignKey(Employee_add, on_delete=models.CASCADE)
    training_date = models.DateField()
    training_type = models.CharField(max_length=20, choices=TRAINING_TYPE)
    training_feedback = models.TextField()    

    def __str__(self):
        return f"{self.employee.first_name} {self.employee.last_name} - {self.training_date}"
    
class Employee_attendance(models.Model):
    employee = models.ForeignKey(Employee_add, on_delete=models.CASCADE)   
    attendance_date = models.DateField()
    attendance_status = models.CharField(max_length=10, choices=ATTENDANCE_STATUS)

    def __str__(self):
        return f"{self.employee.first_name} {self.employee.last_name} - {self.attendance_date}"    