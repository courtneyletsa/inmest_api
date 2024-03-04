# Generated by Django 5.0.1 on 2024-03-04 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0005_remove_imuser_permanant_login_fail_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="imuser",
            name="permanant_login_fail",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="imuser",
            name="temporal_login_fail",
            field=models.IntegerField(default=0),
        ),
    ]