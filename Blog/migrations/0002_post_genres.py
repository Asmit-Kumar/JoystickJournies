# Generated by Django 4.2.3 on 2023-09-14 16:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("Blog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="genres",
            field=models.CharField(
                choices=[
                    ("Shooter", "Shooter"),
                    ("Choice Matters", "Choice Matters"),
                    ("Adventure", "Adventure"),
                    ("Strategy", "Strategy"),
                ],
                default=django.utils.timezone.now,
                max_length=100,
            ),
            preserve_default=False,
        ),
    ]
