# Generated by Django 4.2.7 on 2023-12-04 00:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('picnix_backbone', '0005_clusterinfo_imagecluster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagecluster',
            name='image_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='picnix_backbone.image'),
        ),
    ]
