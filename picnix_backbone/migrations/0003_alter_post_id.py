# Generated by Django 4.2.6 on 2023-12-03 21:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "picnix_backbone",
            "0002_rename_hash_id_image_id_remove_post_file_id_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
