# Generated by Django 4.2.6 on 2023-12-06 20:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("picnix_backbone", "0012_remove_imagecluster_id_alter_imagecluster_image_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="timestamp",
            field=models.IntegerField(),
        ),
    ]
