# Generated by Django 3.2.11 on 2022-02-11 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appToDo', '0012_alter_tarea_fecha_vencimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='titulo_proyecto',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
