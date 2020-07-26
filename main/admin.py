from django.contrib import admin
from .models import student
# Register your models here.

#student model
class StudentAdmin(admin.ModelAdmin):
    fields = ["student_name",
            "student_age",
            "student_email",
            "student_timeofreg"]
admin.site.register(student)
