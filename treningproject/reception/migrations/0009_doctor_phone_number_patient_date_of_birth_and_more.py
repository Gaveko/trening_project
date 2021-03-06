# Generated by Django 4.0.2 on 2022-02-20 08:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reception', '0008_doctor_admission_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='phone_number',
            field=models.CharField(default='099-99-99', max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='date_of_birth',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='email',
            field=models.EmailField(default='afasdf@email.com', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='phone_number',
            field=models.CharField(default='099-99-99', max_length=15),
            preserve_default=False,
        ),
    ]
