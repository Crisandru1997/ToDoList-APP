# Generated by Django 3.2.11 on 2022-01-27 21:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appToDo', '0005_remove_tarea_fecha_mañana'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='titulo_proyecto',
            field=models.ForeignKey(default='Todos', on_delete=django.db.models.deletion.CASCADE, to='appToDo.proyecto'),
        ),
    ]
