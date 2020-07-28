# Generated by Django 3.0 on 2020-07-28 10:05

import datetime
from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_student_student_marks_c'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_DOB',
            field=models.DateField(default=datetime.datetime.now, help_text='Use the button on the right or the arrow keys to edit the date', validators=[main.models.no_Future_Dob, main.models.least_DOB_check], verbose_name='Enter Date of Birth of Student in DD-MM-YYYY format'),
        ),
    ]
