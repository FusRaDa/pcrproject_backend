# Generated by Django 4.0.7 on 2022-10-04 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_remove_batch_labels_batch_miscfields_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='miscFields',
            field=models.JSONField(blank=True, default='hi'),
            preserve_default=False,
        ),
    ]
