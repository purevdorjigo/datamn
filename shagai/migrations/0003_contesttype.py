# Generated by Django 3.2.7 on 2021-09-22 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shagai", "0002_alter_player_team"),
    ]

    operations = [
        migrations.CreateModel(
            name="ContestType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
            ],
        ),
    ]
