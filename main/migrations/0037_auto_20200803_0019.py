# Generated by Django 3.0 on 2020-08-02 18:49

import django.core.validators
from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0036_auto_20200802_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='Mobile_number',
            field=models.CharField(max_length=10, validators=[main.models.checkForAlpha, django.core.validators.MinLengthValidator(10)]),
        ),
    ]