# Generated by Django 5.0.6 on 2024-06-01 03:36

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0009_alter_matches_attendance_alter_matches_away_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="matches",
        ),
        migrations.DeleteModel(
            name="seasons",
        ),
        migrations.DeleteModel(
            name="seasonStats",
        ),
        migrations.DeleteModel(
            name="teams",
        ),
    ]