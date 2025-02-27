from django.db import models

# Create your models here.

#  department
class Department_details(models.Model):
    dept_name=models.CharField(max_length=150)
    dept_description=models.CharField(max_length=180)
    
    def __str__(self):
        return self.dept_name

# designation
class Designation(models.Model):
    designation_name=models.CharField(max_length=100)
    designation_dept=models.ForeignKey(Department_details,on_delete=models.CASCADE)
    designation_description=models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return self.designation_name
    

# employee
class Employee_details(models.Model):
    
    name=models.CharField(max_length=200)
    gender_choices=[
        ('M','Male'),
        ('F','Female'),
        ('O','Other')
    ]
    gender=models.CharField(max_length=1,choices=gender_choices)
    dob=models.DateField()
    address=models.CharField(max_length=200)
    email=models.EmailField(unique=True)
    department=models.ForeignKey(Department_details,on_delete=models.SET_NULL,null=True)
    designation=models.ForeignKey(Designation,on_delete=models.SET_NULL,null=True)
    doj=models.DateField()
    image=models.ImageField(upload_to='image/')
    
    def __str__(self) -> str:
        return self.name
