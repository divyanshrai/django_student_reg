from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from datetime import datetime,date,timedelta
from django.utils import timezone as tz
from django.forms import ValidationError
from django.utils.crypto import get_random_string

''' Validators Methods that help validate the fields
checkfordigits(s) - Checks each letter for digits
no_Future_Dob(value) - Ensures DOB is not in the future

 '''

def checkForDigits(value):
    for character in value:
        if character.isdigit():
            raise ValidationError('Name cannot contain a digit.')

def checkForAlpha(value):
    for character in value:
        if not character.isdigit():
            raise ValidationError('Phone can only contain digits.')

def no_Future_Dob(value):
    today = date.today()
    if value > today:
        raise ValidationError('A date of birth cannot be in the future.')

def least_DOB_check(value):
    least_Age=3
    week_gap=least_Age*52
    now=date.today()
    least_date=now-timedelta(weeks=week_gap)
    if value > least_date:
        raise ValidationError('Your child needs to be at least 3 years old')

def max_DOB_check(value):
    max_Age=60
    week_gap=max_Age*52
    now=date.today()
    max_date=now-timedelta(weeks=week_gap)
    if value < max_date:
        raise ValidationError('We are currently not accepting students over 50 years of age')

def get_random():
    return    get_random_string(length=10,
                              allowed_chars='ABCDEFGHJKLMNPQUSTWXYZ123456789')


# Create your models here.
class student(models.Model):
    student_Unique_ID = models.CharField(max_length=10,
                                        help_text="Please save this number, this will be used to unique identify the student",
                                        default=get_random,
                                        primary_key=True)
    student_First_Name=models.TextField(validators=[checkForDigits])
    student_Last_Name=models.TextField(validators=[checkForDigits])
                                    
    student_email=models.TextField(null=True,
                                blank=True)
    
    student_mobile_number=models.CharField(max_length=10,
                                validators=[checkForAlpha],
                                null=True,
                                blank=True)

    student_DOB=models.DateField("Enter Date of Birth of Student in DD-MM-YYYY format",
                                default=datetime.now,
                                validators=[no_Future_Dob,
                                    least_DOB_check,
                                    max_DOB_check],
                                help_text="Use the button on the right or the arrow keys to edit the date")

    student_timeofreg=models.DateTimeField(default=datetime.now)

    student_img=models.ImageField("Upload an image of the student",
                                blank=True,upload_to="images/",
                                default='default/blank_user.png')

    student_marks_A=models.DecimalField(max_digits=5,
                                        decimal_places=2,
                                        validators=[MaxValueValidator(100.00),
                                        MinValueValidator(0.00)],
                                        default=0.00)

    student_marks_B=models.DecimalField(max_digits=5,
                                        decimal_places=2,
                                        validators=[MaxValueValidator(100.00),
                                        MinValueValidator(0.00)],
                                        default=0.00)

    student_marks_C=models.DecimalField(max_digits=5,
                                        decimal_places=2,
                                        validators=[MaxValueValidator(100.00),
                                        MinValueValidator(0.00)],
                                        default=0.00)
 
    guardian_First_Name=models.TextField(validators=[checkForDigits])
    guardian_Last_Name=models.TextField(validators=[checkForDigits])
    guardian_email=models.TextField()
    guardian_mobile_number=models.CharField(max_length=10,
                                validators=[checkForAlpha])
    

    def __str__(self):
        return self.student_First_Name

    class Meta:
        unique_together = (("guardian_mobile_number", "student_First_Name","student_Last_Name"),)
