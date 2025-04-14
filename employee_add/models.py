from django.db import models

class Employee_add(models.Model):
    Employee_type =[
        ('Full time','Full time'),
        ('Part time','Part time'),
        ('Contract','Contract'),
        ('Intern','Intern'),
    ]
    Gender_choices=[
        ('Male','Male'),
        ('Female','Female')
    ]

    id=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=15,blank=True,null=True)
    Date_of_Birth=models.DateField
    Gender=models.CharField(max_length=10,choices=Gender_choices)
    Address=models.TextField()

    Job_title=models.CharField(max_length=50)
    Department=models.CharField(max_length=50)
    Employee_type=models.CharField(max_length=10,choices=Employee_type) 
    Salary=models.DecimalField(max_digits=10,decimal_places=2)
    Date_hired=models.DateField()

    profile_picture=models.ImageField(upload_to='employee_pics/' ,blank=True,null=True)
    resume=models.FileField(upload_to='resume/', blank=True,null=True)

    is_active=models.BooleanField(default=True)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.Job_title}"


