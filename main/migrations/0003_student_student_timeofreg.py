# Generated by Django 3.0 on 2020-07-25 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200726_0013'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_timeofreg',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
