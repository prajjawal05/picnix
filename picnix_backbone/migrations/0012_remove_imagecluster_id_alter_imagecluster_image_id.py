# Generated by Django 4.2.6 on 2023-12-04 19:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("picnix_backbone", "0011_alter_imagecluster_unique_together"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="imagecluster",
            name="id",
        ),
        migrations.AlterField(
            model_name="imagecluster",
            name="image_id",
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
