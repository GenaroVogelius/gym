# Generated by Django 4.2 on 2023-09-14 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("power_app", "0016_alter_usuario_celular"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usuario",
            name="DNI",
            field=models.BigIntegerField(unique=True),
        ),
    ]
