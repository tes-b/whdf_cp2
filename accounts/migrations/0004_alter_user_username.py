# Generated by Django 4.1 on 2023-01-31 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_alter_user_managers_alter_user_gender_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
