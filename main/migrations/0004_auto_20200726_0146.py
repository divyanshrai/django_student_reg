# Generated by Django 3.0 on 2020-07-25 20:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_student_student_timeofreg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_timeofreg',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
