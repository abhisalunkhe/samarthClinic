# Generated by Django 4.1 on 2024-04-01 04:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0003_contact"),
    ]

    operations = [
        migrations.AddField(
            model_name="appointment",
            name="isDone",
            field=models.BooleanField(default=False),
        ),
    ]