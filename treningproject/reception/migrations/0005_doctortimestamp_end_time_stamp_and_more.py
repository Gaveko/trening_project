# Generated by Django 4.0.2 on 2022-02-19 06:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reception', '0004_doctorday_doctor_doctortimestamp_doctor_day'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctortimestamp',
            name='end_time_stamp',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctortimestamp',
            name='is_busy',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='doctortimestamp',
            name='start_time_stamp',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
