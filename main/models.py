from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from datetime import datetime

# Create your models here.
class student(models.Model):
    student_name=models.CharField(max_length=100)
    student_age=models.IntegerField(validators=[MaxValueValidator(200),
                                    MinValueValidator(1)])
    student_email=models.CharField(max_length=200)
    student_DOB=models.DateField(default=datetime.now)
    student_timeofreg=models.DateTimeField(default=datetime.now)
    student_img=models.ImageField(blank=True,upload_to="images/",default='default/blank_user.png')

    def __str__(self):
        return self.student_name