# Generated by Django 4.0.2 on 2022-02-19 06:26
import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reception', '0002_doctor_patient_alter_recordtodoctor_doctor_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='DoctorTimeStamp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='doctor',
            name='end_work_time',
            field=models.TimeField(default=datetime.datetime.now()),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctor',
            name='start_work_time',
            field=models.TimeField(default=datetime.datetime.now()),
            preserve_default=False,
        ),
    ]
