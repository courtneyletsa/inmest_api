# Generated by Django 5.0.1 on 2024-02-13 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ClassAttendance",
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
                ("is_present", models.BooleanField(default=False)),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("date_modified", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="ClassSchedule",
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
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True, default="N/A", null=True)),
                ("start_date_and_time", models.DateTimeField()),
                ("end_date_and_time", models.DateTimeField()),
                ("is_repeated", models.BooleanField(default=False)),
                ("repeat_frequency", models.IntegerField()),
                ("is_active", models.BooleanField(default=False)),
                ("organizer", models.CharField(max_length=255)),
                ("venue", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Course",
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
                ("name", models.CharField(max_length=1000)),
                ("description", models.TextField(blank=True, default="N/A", null=True)),
                ("date_created", models.DateTimeField(auto_now_add=True, null=True)),
                ("date_modified", models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Query",
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
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True, default="N/A", null=True)),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("date_modified", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="QueryComment",
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
                ("comment", models.TextField(blank=True, default="N/A", null=True)),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("date_modified", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="ResolutionStatus",
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
                ("resolution_status", models.CharField(max_length=225, unique=True)),
            ],
        ),
    ]
