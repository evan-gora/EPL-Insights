# Generated by Django 5.0.6 on 2024-07-02 16:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("predictions", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="upcomingmatches",
            name="week",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
