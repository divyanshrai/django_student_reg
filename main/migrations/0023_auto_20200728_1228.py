# Generated by Django 3.0 on 2020-07-28 06:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_auto_20200728_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_marks_A',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5, validators=[django.core.validators.MaxValueValidator(100.0), django.core.validators.MinValueValidator(0.0)]),
        ),
    ]