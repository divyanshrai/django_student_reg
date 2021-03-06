# Generated by Django 3.0 on 2020-08-02 18:50

import django.core.validators
from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0037_auto_20200803_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='guardian_mobile_number',
            field=models.CharField(max_length=10, validators=[main.models.checkForAlpha, django.core.validators.MinLengthValidator(10)]),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_mobile_number',
            field=models.CharField(blank=True, max_length=10, null=True, validators=[main.models.checkForAlpha, django.core.validators.MinLengthValidator(10)]),
        ),
    ]
