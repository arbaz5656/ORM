from django.db import models

# Create your models here.

# Department
class Department(models.Model):
    department=models.CharField(max_length=100)

    def __str__(self):
        return self.department

    class Meta:
        ordering=['department']


# Student id
class StudentId(models.Model):
    student_id=models.CharField(max_length=100)

    def __str__(self):
        return self.student_id


# Student
class Student(models.Model):
    department=models.ForeignKey(Department,related_name="depart" , on_delete=models.CASCADE)
    student_id=models.OneToOneField(StudentId,related_name="studentid",on_delete=models.CASCADE)
    student_name=models.CharField(max_length=100)
    student_email=models.EmailField(unique=True)
    student_age=models.IntegerField(default=18)
    student_address=models.TextField()


    def __str__(self):
        return self.student_name

    class Meta:
        ordering=['student_name']
        verbose_name="student"

