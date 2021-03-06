# Generated by Django 3.2.5 on 2021-08-26 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employer', '0004_alter_job_salary'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=50)),
                ('l_name', models.CharField(max_length=50)),
                ('company_name', models.CharField(max_length=100)),
                ('company_id', models.CharField(max_length=100)),
                ('experience', models.IntegerField(max_length=50)),
                ('contact', models.TextField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female'), ('TG', 'TG')], default='male', max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='job',
            name='experience',
            field=models.CharField(max_length=50),
        ),
    ]
