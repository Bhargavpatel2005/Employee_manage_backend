# Generated by Django 5.2 on 2025-05-01 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_add', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_job',
            name='job_max_salary',
            field=models.IntegerField(max_length=20),
        ),
        migrations.AlterField(
            model_name='post_job',
            name='job_min_salary',
            field=models.IntegerField(max_length=20),
        ),
    ]
