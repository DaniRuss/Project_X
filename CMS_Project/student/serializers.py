from rest_framework import serializers
from django.contrib.auth.models import User

# from rest_framework import serializers
from .models import Student_table

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_table
        fields = '__all__'  # Include all fields
        # ('student_name','father_name') if we want to send spacific data