# Generated by Django 4.1.1 on 2022-10-05 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Personas', '0002_rename_fecha_persona_fecha_de_creacion_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persona',
            name='fecha_de_creacion',
        ),
        migrations.AddField(
            model_name='persona',
            name='fecha_de_nacimiento',
            field=models.IntegerField(null=True),
        ),
    ]