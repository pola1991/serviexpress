# Generated by Django 4.0.4 on 2022-11-07 22:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_hora_reserva_horas'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reserva',
            old_name='horas',
            new_name='hora',
        ),
    ]
