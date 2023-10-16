# Generated by Django 4.2.5 on 2023-10-02 02:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("logcutting_loglist", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="LogList",
            fields=[
                (
                    "log_id",
                    models.CharField(
                        max_length=100, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("partai_id", models.CharField(max_length=100)),
                ("tanggal_kedatangan", models.DateField()),
                ("supplier_id", models.CharField(max_length=100)),
                ("grade", models.CharField(max_length=100)),
                ("species_id", models.CharField(max_length=100)),
                ("log_colour", models.CharField(max_length=100)),
                ("log_length", models.IntegerField()),
                ("diameter_1", models.IntegerField()),
                ("diameter_2", models.IntegerField()),
                ("average_diameter", models.IntegerField()),
                ("volume_bruto", models.IntegerField()),
                ("volume_trimming", models.IntegerField()),
                ("volume_netto", models.IntegerField()),
                ("is_deleted", models.BooleanField(default=False)),
            ],
            options={
                "db_table": 'log_cutting"."log_list_test',
            },
        ),
        migrations.DeleteModel(
            name="Transaction",
        ),
    ]
