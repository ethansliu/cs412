# Generated by Django 5.1.3 on 2024-11-22 16:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("project", "0004_outfit_outfitname"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sell",
            name="platform",
            field=models.IntegerField(),
        ),
    ]
