# Generated by Django 5.1.3 on 2024-11-22 17:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("project", "0006_alter_sell_platform"),
    ]

    operations = [
        migrations.AlterField(
            model_name="outfit",
            name="bottom",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="bottom",
                to="project.clothes",
            ),
        ),
        migrations.AlterField(
            model_name="outfit",
            name="outerwear",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="outerwear",
                to="project.clothes",
            ),
        ),
        migrations.AlterField(
            model_name="outfit",
            name="shoes",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="shoes",
                to="project.clothes",
            ),
        ),
        migrations.AlterField(
            model_name="outfit",
            name="top",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="top",
                to="project.clothes",
            ),
        ),
    ]
