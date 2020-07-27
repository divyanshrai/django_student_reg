from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from datetime import datetime,date
from django.utils import timezone as tz
from django.forms import ValidationError

''' Validators Methods that help validate the fields
checkfordigits(s) - Checks each letter for digits
no_Future_Dob(value) - Ensures DOB is not in the future


 '''
def checkForDigits(value):
    for character in value:
        if character.isdigit():
            raise ValidationError('Name cannot contain a digit.')

def no_Future_Dob(value):
    today = date.today()
    if value > today:
        raise ValidationError('A date of birth cannot be in the future.')


# Create your models here.
class student(models.Model):
    student_name=models.CharField(max_length=100,
                                validators=[checkForDigits])

    student_age=models.IntegerField(validators=[MaxValueValidator(200),
                                    MinValueValidator(1)])
                                    
    student_email=models.CharField(max_length=200)

    student_DOB=models.DateField("Enter Date of Birth of Student in DD-MM-YYYY format",
                                default=datetime.now,
                                validators=[no_Future_Dob],
                                help_text="Use the button on the right or the arrow keys to edit the date")

    student_timeofreg=models.DateTimeField(default=datetime.now)

    student_img=models.ImageField("Upload an image of the student",
                                blank=True,upload_to="images/",
                                default='default/blank_user.png')

    def __str__(self):
        return self.student_name