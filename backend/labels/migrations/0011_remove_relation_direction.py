# Generated by Django 4.0.2 on 2022-03-02 01:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("labels", "0010_rename_relationnew_relation"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="relation",
            name="direction",
        ),
    ]