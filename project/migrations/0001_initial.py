# Generated by Django 5.1.3 on 2024-11-22 16:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Closet",
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
                ("firstName", models.TextField()),
                ("lastName", models.TextField()),
                ("favoriteStyle", models.TextField()),
                ("favoriteBrand", models.TextField()),
                ("userWeight", models.TextField()),
                ("userHeight", models.TextField()),
                ("shirtSize", models.TextField()),
                ("pantSize", models.TextField()),
                ("outerwearSize", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Category",
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
                ("categoryName", models.TextField()),
                (
                    "closet",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="project.closet"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Clothes",
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
                ("timestamp", models.DateTimeField(auto_now=True)),
                ("brand", models.TextField()),
                ("color", models.TextField()),
                ("image", models.ImageField(blank=True, upload_to="")),
                ("price", models.IntegerField()),
                ("size", models.TextField()),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="project.category",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Outfit",
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
                ("outfitCreated", models.DateTimeField(auto_now=True)),
                (
                    "bottom",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="bottom",
                        to="project.clothes",
                    ),
                ),
                (
                    "outerwear",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="outerwear",
                        to="project.clothes",
                    ),
                ),
                (
                    "shoes",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="shoes",
                        to="project.clothes",
                    ),
                ),
                (
                    "top",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="top",
                        to="project.clothes",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Sell",
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
                ("platform", models.ImageField(blank=True, upload_to="")),
                ("sellPrice", models.IntegerField()),
                (
                    "item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="project.clothes",
                    ),
                ),
            ],
        ),
    ]
