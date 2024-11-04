# forms.py
from django import forms
from .models import student

class StudentForm(forms.ModelForm):
    class Meta:
        model = student
        fields = ['Student_name','father_name', 'age', 'gender','email',]  # Include other fields as necessary