# Generated by Django 5.1.3 on 2024-11-22 17:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("project", "0009_alter_outfit_bottom_alter_outfit_outerwear_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sell",
            name="platform",
            field=models.TextField(blank=True),
        ),
    ]
