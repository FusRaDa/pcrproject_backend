# Generated by Django 4.0.7 on 2022-10-16 14:53

import base.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0042_alter_batch_fieldlabels'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='fieldLabels',
            field=models.JSONField(blank=True, default=base.models.get_default_miscFields, null=True),
        ),
    ]
