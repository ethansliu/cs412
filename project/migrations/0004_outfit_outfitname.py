# Generated by Django 5.1.3 on 2024-11-22 16:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("project", "0003_category_clothes_outfit_sell"),
    ]

    operations = [
        migrations.AddField(
            model_name="outfit",
            name="outfitName",
            field=models.TextField(default="Outfit"),
            preserve_default=False,
        ),
    ]