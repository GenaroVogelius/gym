# Generated by Django 4.2 on 2023-04-14 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("power_app", "0004_alter_usuario_pago"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usuario",
            name="activo",
            field=models.BooleanField(default=True, editable=False),
        ),
    ]