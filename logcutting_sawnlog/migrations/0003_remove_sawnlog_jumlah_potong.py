# Generated by Django 4.2.5 on 2023-10-09 10:06

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("logcutting_sawnlog", "0002_sawnlog_delete_transaction"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="sawnlog",
            name="jumlah_potong",
        ),
    ]
