# Generated by Django 3.2.11 on 2022-01-27 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appToDo', '0004_tarea_fecha_mañana'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tarea',
            name='fecha_mañana',
        ),
    ]
