# Generated by Django 4.2.6 on 2023-11-25 03:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("picnix_backbone", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="image",
            old_name="hash_id",
            new_name="id",
        ),
        migrations.RemoveField(
            model_name="post",
            name="file_id",
        ),
        migrations.AddField(
            model_name="post",
            name="description",
            field=models.TextField(default="", max_length=100),
        ),
        migrations.AddField(
            model_name="post",
            name="image_id",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="picnix_backbone.image",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="post",
            name="user",
            field=models.TextField(default="", max_length=20),
            preserve_default=False,
        ),
    ]
