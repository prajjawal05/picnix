# Generated by Django 4.2.6 on 2023-12-04 07:08

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("picnix_backbone", "0010_image_num_refs_post_timestamp_and_more"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="imagecluster",
            unique_together=set(),
        ),
    ]
