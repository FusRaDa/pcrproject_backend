# Generated by Django 4.0.7 on 2022-11-14 15:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0071_alter_batch_batchdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='batchDate',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 14, 10, 51, 16, 609956)),
        ),
    ]