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
                'student_DOB')
    
    def clean_student_name(self):
        student_name = self.cleaned_data['student_name']
        #### checking if name field has digits ####
        if checkfordigits(student_name):
            raise ValidationError('Name cannot contain a digit')

        return student_name
        
    
''' Methods that help validate the fields
checkfordigits(s) - Checks each letter for digits


 '''

def checkfordigits(s):
    for character in s:
        if character.isdigit():
            return True
    return False