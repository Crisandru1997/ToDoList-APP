# Generated by Django 3.2.11 on 2022-01-27 17:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appToDo', '0003_auto_20220127_1312'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarea',
            name='fecha_mañana',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 28, 14, 39, 10, 488509)),
        ),
    ]
