# Generated by Django 4.1 on 2024-04-01 04:46

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0004_appointment_isdone"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Doctors",
            new_name="Doctor",
        ),
    ]
