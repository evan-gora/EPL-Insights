# Generated by Django 5.0.6 on 2024-05-31 21:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="matches",
            old_name="attendance",
            new_name="Attendance",
        ),
        migrations.RenameField(
            model_name="matches",
            old_name="away",
            new_name="Away",
        ),
        migrations.RenameField(
            model_name="matches",
            old_name="date",
            new_name="Date",
        ),
        migrations.RenameField(
            model_name="matches",
            old_name="home",
            new_name="Home",
        ),
        migrations.RenameField(
            model_name="matches",
            old_name="season",
            new_name="Season",
        ),
        migrations.RenameField(
            model_name="matches",
            old_name="venue",
            new_name="Venue",
        ),
        migrations.RenameField(
            model_name="seasonstats",
            old_name="passAtt",
            new_name="Att",
        ),
        migrations.RenameField(
            model_name="seasonstats",
            old_name="corners",
            new_name="CK",
        ),
        migrations.RenameField(
            model_name="seasonstats",
            old_name="passCmp",
            new_name="Cmp",
        ),
        migrations.RenameField(
            model_name="seasonstats",
            old_name="reds",
            new_name="CrdR",
        ),
        migrations.RenameField(
            model_name="seasonstats",
            old_name="yellows",
            new_name="CrdY",
        ),
        migrations.RenameField(
            model_name="seasonstats",
            old_name="draws",
            new_name="D",
        ),
        migrations.RenameField(
            model_name="seasonstats",
            old_name="freeK",
            new_name="FK",
        ),
        migrations.RenameField(
            model_name="seasonstats",
            old_name="fouls",
            new_name="Fls",
        ),
        migrations.RenameField(
            model_name="seasonstats",
            old_name="goalsA",
            new_name="GA",
        ),
        migrations.RenameField(
            model_name="seasonstats",
            old_name="goalsF",
            new_name="GF",
        ),
        migrations.RenameField(
            model_name="seasonstats",
            old_name="losses",
            new_name="L",
        ),
        migrations.RenameField(
            model_name="seasonstats",
            old_name="ownGoals",
            new_name="OG",
        ),
        migrations.RenameField(
            model_name="seasonstats",
            old_name="PKGoals",
            new_name="PK",
        ),
        migrations.RenameField(
            model_name="seasonstats",
            old_name="PKCon",
            new_name="PKcon",
        ),
        migrations.RenameField(
            model_name="seasonstats",
            old_name="points",
            new_name="Pts",
        ),
        migrations.RenameField(
            model_name="seasonstats",
            old_name="season",
            new_name="Season",
        ),
        migrations.RenameField(
            model_name="seasonstats",
            old_name="shots",
            new_name="Sh",
        ),
        migrations.RenameField(
            model_name="seasonstats",
            old_name="shotsOT",
            new_name="SoT",
        ),
        migrations.RenameField(
            model_name="seasonstats",
            old_name="squad",
            new_name="Squad",
        ),
        migrations.RenameField(
            model_name="seasonstats",
            old_name="wins",
            new_name="W",
        ),
        migrations.RemoveField(
            model_name="seasonstats",
            name="passPerc",
        ),
        migrations.AddField(
            model_name="seasonstats",
            name="CmpPerc",
            field=models.DecimalField(
                db_column="Cmp%", decimal_places=1, default=0, max_digits=4
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="matches",
            name="awayGoals",
            field=models.IntegerField(db_column="Away Goals"),
        ),
        migrations.AlterField(
            model_name="matches",
            name="awayxG",
            field=models.DecimalField(db_column="xG.1", decimal_places=1, max_digits=3),
        ),
        migrations.AlterField(
            model_name="matches",
            name="homeGoals",
            field=models.IntegerField(db_column="Home Goals"),
        ),
        migrations.AlterField(
            model_name="matches",
            name="homexG",
            field=models.DecimalField(db_column="xG", decimal_places=1, max_digits=3),
        ),
    ]
