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
        fields = (#'student_Unique_ID',
                'student_First_Name',
                'student_Last_Name',
                'student_mobile_number',
                'student_email',
                'student_DOB',
                'student_marks_A',
                'student_marks_B',
                'student_marks_C',
                'student_img',
                'guardian_First_Name',
                'guardian_Last_Name',
                'guardian_mobile_number',
                'guardian_email',
                )
    def __init__(self, *args, **kwargs): 
        super(RegisterForm, self).__init__(*args, **kwargs)                       
 #       self.fields['student_Unique_ID'].disabled = True
