# Generated by Django 4.0.2 on 2022-02-20 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reception', '0009_doctor_phone_number_patient_date_of_birth_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='date_of_birth',
            field=models.DateField(),
        ),
    ]
