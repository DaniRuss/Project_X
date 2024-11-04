from django.shortcuts import render
from django.http import HttpResponse
from .models import Student_table
from django.template import loader

from django.contrib.auth.models import User  # tis id for API
from rest_framework import viewsets  #   this is for the API  
from student.serializers import StudentSerializer  # this is for API
#
class Studentviewset(viewsets.ModelViewSet):
    queryset = Student_table.objects.all()
    serializer_class = StudentSerializer







































# Create your views here.
# def home(request): #to fach from database table 
#     Student_List = Student_table.objects.all()
#     context={'Student_List': Student_List} #table name 
#     return render(request,'home.html',context=context)
def Student(request):
    if request.method == 'POST':
        Student_name = request.POST['Student_name']
        father_name = request.POST['father_name']
        age = request.POST['age']
        gender = request.POST['gender']
        email = request.POST['email']
        # adding to table
        new_student = Student_table(Student_name=Student_name, father_name=father_name, age=age, gender=gender, email=email)
        new_student.save()
    return render(request, 'home.html')
# to view (not working)
# def view_students(request):
#     students = Student_table.objects.all()  # Retrieve all student records
#     return render(request, 'view_students.html', {'students': students})
# def home(request): # fach(display) form temp/home.html
#     templete = loader.get_template('home.html')
#     return HttpResponse(templete.render())

# def home1(request): # fach(display) form temp/home.html (second option)
#     return render(request, 'home.html')