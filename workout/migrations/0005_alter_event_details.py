# Generated by Django 5.1.4 on 2025-01-18 04:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("workout", "0004_event"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="details",
            field=models.TextField(blank=True, default="", max_length=500, null=True),
        ),
    ]
