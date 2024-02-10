# Generated by Django 5.0.1 on 2024-02-07 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0002_alter_course_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="date_created",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="course",
            name="date_modified",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name="course",
            name="description",
            field=models.TextField(blank=True, default="N/A", null=True),
        ),
    ]