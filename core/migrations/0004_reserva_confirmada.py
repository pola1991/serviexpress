# Generated by Django 4.0.4 on 2022-11-08 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_horas_reserva_hora'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='confirmada',
            field=models.BooleanField(default=False),
        ),
    ]
