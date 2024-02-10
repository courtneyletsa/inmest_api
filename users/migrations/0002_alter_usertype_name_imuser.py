# Generated by Django 5.0.1 on 2024-02-10 10:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usertype",
            name="name",
            field=models.CharField(max_length=225, unique=True),
        ),
        migrations.CreateModel(
            name="IMUser",
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
                ("first_name", models.CharField(max_length=500)),
                ("last_name", models.CharField(max_length=500)),
                ("is_active", models.BooleanField(default=False)),
                (
                    "user_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="users.usertype"
                    ),
                ),
            ],
        ),
    ]