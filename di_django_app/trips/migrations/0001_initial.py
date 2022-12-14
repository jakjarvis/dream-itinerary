# Generated by Django 4.1 on 2022-11-12 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Activity",
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
                ("title", models.CharField(max_length=200)),
                ("description", models.TextField(blank=True)),
                ("dates", models.CharField(blank=True, max_length=50)),
                ("parent_trip", models.CharField(blank=True, max_length=200)),
                (
                    "thumbnail_image",
                    models.ImageField(blank=True, upload_to="trips/images/"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Trip",
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
                ("title", models.CharField(max_length=200)),
                ("description", models.TextField(blank=True)),
                ("dates", models.CharField(blank=True, max_length=50)),
                (
                    "splash_image",
                    models.ImageField(blank=True, upload_to="trips/images/"),
                ),
                (
                    "thumbnail_image",
                    models.ImageField(blank=True, upload_to="trips/images/"),
                ),
            ],
        ),
    ]
