# Generated by Django 4.1.1 on 2022-10-05 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Personas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='persona',
            old_name='fecha',
            new_name='fecha_de_creacion',
        ),
        migrations.AlterField(
            model_name='persona',
            name='apellido',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='persona',
            name='nombre',
            field=models.CharField(max_length=20),
        ),
    ]
