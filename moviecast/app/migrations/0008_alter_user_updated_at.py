# Generated by Django 4.1.4 on 2023-01-20 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0007_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="updated_at",
            field=models.DateTimeField(),
        ),
    ]
