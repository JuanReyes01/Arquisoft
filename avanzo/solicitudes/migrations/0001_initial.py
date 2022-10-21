# Generated by Django 3.2.6 on 2022-10-01 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.IntegerField()),
                ('interes', models.FloatField()),
                ('plazo', models.IntegerField()),
                ('estado', models.BooleanField()),
                ('cliente', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='clientes.cliente')),
            ],
        ),
    ]