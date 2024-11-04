from django.db import models

class Student_table(models.Model):
    # id = models.AutoField(primary_key=True)
    Student_name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    age = models.PositiveBigIntegerField()
    gender = models.CharField(max_length=10,
    choices=[
        ('M', 'Male'),
        ('F', 'Female'),
    ],)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.Student_name} {self.father_name} {self.age}"