# Generated by Django 3.0 on 2020-07-27 02:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20200726_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_DOB',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Enter Date of Birth of Student'),
        ),
    ]