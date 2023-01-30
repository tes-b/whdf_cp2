# Generated by Django 4.1 on 2023-01-28 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_user_gender"),
    ]

    operations = [
        migrations.AlterModelManagers(name="user", managers=[],),
        migrations.AlterField(
            model_name="user",
            name="gender",
            field=models.CharField(
                choices=[("Male", "male"), ("Female", "female"), ("Other", "other")],
                max_length=10,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="is_staff",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="user",
            name="is_superuser",
            field=models.BooleanField(default=False),
        ),
    ]