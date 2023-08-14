


from django.db import models

from django.contrib.auth.models import AbstractUser


class Student(AbstractUser):
    full_name = models.CharField(max_length=50)
    selected_course = models.CharField(max_length=50)
    parent_no = models.CharField(max_length=13)
    phone = models.CharField(max_length=13)
    dob = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class WaitingList(models.Model):
    student= models.OneToOneField(Student, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)
    username=models.CharField(max_length=100)
    phone=models.CharField(max_length=13)
    selected_course = models.CharField(max_length=50)

    def __str__(self):
        return self.student.username




    
    

class Batch(models.Model):
    options=(
        ("PYTHON","PYTHON"),
        ("TABLOAU","TABLOAU"),
        ("DATA SCIENCE","DATA SCIENCE"),
        ("ASP.net","ASP.net"),
        ("FLUTTER","FLUTTER"),
        ("MEA(R)N","MEA(R)N"),
        ("TESTING","TESTING"),
    )
    batch_name = models.CharField(max_length=100)
    batch_code = models.CharField(max_length=20, unique=True)
    start_date = models.DateField()
    coursename=models.CharField(max_length=100,choices=options,default="PYTHON")


    def __str__(self):
        return self.batch_name


class AddStudent(models.Model):
   
    stud=models.ForeignKey(Student,on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)

   
   

    

   




    


    
