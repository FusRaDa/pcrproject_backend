# Generated by Django 4.0.7 on 2022-10-05 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0023_rename_groupassay_batch_assay'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='miscFields',
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
    ]
