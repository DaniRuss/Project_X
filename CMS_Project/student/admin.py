from django.contrib import admin
from .models import Student_table
# Register your models here.


class studentadmin(admin.ModelAdmin):
    list_display = ("Student_name","father_name", "age", "gender")

admin.site.register(Student_table, studentadmin)
