# Generated by Django 5.1.2 on 2024-10-21 17:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mini_fb", "0002_statusmessage"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="image_url",
        ),
        migrations.AddField(
            model_name="profile",
            name="image_file",
            field=models.ImageField(blank=True, upload_to=""),
        ),
    ]