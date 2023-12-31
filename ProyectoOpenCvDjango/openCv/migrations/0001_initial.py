# Generated by Django 4.2.7 on 2023-11-11 03:25

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Usuario",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=100)),
                ("datos_biometricos_hashed", models.TextField()),
                ("datos_biometricos_salt", models.CharField(max_length=50)),
                ("imagen_rostro", models.ImageField(upload_to="rostros/")),
            ],
        ),
    ]
