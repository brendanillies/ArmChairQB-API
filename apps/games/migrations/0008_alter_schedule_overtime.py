# Generated by Django 4.2.5 on 2023-10-02 22:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("games", "0007_alter_schedule_overtime"),
    ]

    operations = [
        migrations.AlterField(
            model_name="schedule",
            name="overtime",
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
    ]