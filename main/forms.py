from django import forms
from django.forms import ValidationError
from main.models import student

class DateInput(forms.DateInput):
    input_type = 'date'

class EmailInput(forms.EmailInput):
    pass

class RegisterForm(forms.ModelForm):
    class Meta:
        model = student
        widgets = {
            'student_DOB': DateInput(),
            'student_email':EmailInput(),
        }
        fields = ('student_name',
                'student_age',
                'student_email',
                'student_img',
                'student_DOB',
                'student_marks_A',
                'student_marks_B',
                'student_marks_C',)