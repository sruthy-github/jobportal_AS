# Generated by Django 3.2.5 on 2021-08-25 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employer', '0002_rename_end_end_job_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='end_date',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='job',
            name='start_date',
            field=models.CharField(max_length=15),
        ),
    ]