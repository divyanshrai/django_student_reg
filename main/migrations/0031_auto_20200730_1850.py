# Generated by Django 3.0 on 2020-07-30 13:20

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0030_auto_20200730_1746'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='student_name',
            new_name='student_First_Name',
        ),
        migrations.AddField(
            model_name='student',
            name='guardian_email',
            field=models.TextField(default='awdw@jadn.com'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='guardian_mobile_number',
            field=models.CharField(default=123456789, max_length=10, validators=[main.models.checkForAlpha]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='student_Last_Name',
            field=models.TextField(default='commonlastname', validators=[main.models.checkForDigits]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='student_mobile_number',
            field=models.CharField(blank=True, max_length=10, null=True, validators=[main.models.checkForAlpha]),
        ),
        migrations.AlterUniqueTogether(
            name='student',
            unique_together=set(),
        ),
    ]
