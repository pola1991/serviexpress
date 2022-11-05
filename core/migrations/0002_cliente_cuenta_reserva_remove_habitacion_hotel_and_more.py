# Generated by Django 4.0.4 on 2022-11-04 22:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID CLIENTE')),
                ('nombre_completo', models.CharField(max_length=40, verbose_name='NOMBRE COMPLETO')),
                ('rut', models.IntegerField(verbose_name='RUT')),
                ('dv_rut', models.IntegerField(verbose_name='DIGITO VERIFICADOR')),
                ('correo', models.EmailField(max_length=254, verbose_name='MAIL')),
            ],
        ),
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('id_cuenta', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID CUENTA')),
                ('usuario', models.CharField(max_length=30, verbose_name='USUARIO')),
                ('correo', models.EmailField(max_length=254, verbose_name='MAIL')),
                ('password', models.CharField(max_length=20, verbose_name='PASSWORD')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id_reserva', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID RESERVA')),
                ('fecha', models.DateTimeField(blank=True, null=True, verbose_name='FECHA')),
                ('hora', models.IntegerField(choices=[[0, '8:00hrs. - 8:59hrs.'], [1, '9:00hrs. - 9:59hrs.'], [2, '10:00hrs. - 10:59hrs.'], [3, '11:00hrs. - 11:59hrs.'], [4, '12:00hrs. - 12:59hrs.'], [5, '13:00hrs. - 13:59hrs.'], [6, '14:00hrs. - 14:59hrs.']], verbose_name='HORA')),
                ('cuenta', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.cuenta')),
            ],
        ),
        migrations.RemoveField(
            model_name='habitacion',
            name='hotel',
        ),
        migrations.RemoveField(
            model_name='habitacion',
            name='tipo_habitacion',
        ),
        migrations.RemoveField(
            model_name='servicio',
            name='descripcion_servicio',
        ),
        migrations.RemoveField(
            model_name='servicio',
            name='hotel',
        ),
        migrations.RemoveField(
            model_name='servicio',
            name='tipo_servicio',
        ),
        migrations.AddField(
            model_name='servicio',
            name='precio',
            field=models.IntegerField(null=True, verbose_name='PRECIO'),
        ),
        migrations.AddField(
            model_name='servicio',
            name='tipo',
            field=models.CharField(max_length=30, null=True, verbose_name='TIPO'),
        ),
        migrations.DeleteModel(
            name='Administrador',
        ),
        migrations.DeleteModel(
            name='Habitacion',
        ),
        migrations.DeleteModel(
            name='Hotel',
        ),
        migrations.DeleteModel(
            name='Tipo_habitacion',
        ),
        migrations.DeleteModel(
            name='Tipo_servicio',
        ),
        migrations.AddField(
            model_name='reserva',
            name='servicio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.servicio', verbose_name='SERVICIO'),
        ),
    ]
