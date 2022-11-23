# Generated by Django 4.0.7 on 2022-11-17 22:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0074_alter_batch_batchdate_alter_batch_dna_extraction_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='batchDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 17, 17, 49, 5, 450753)),
        ),
        migrations.AlterField(
            model_name='batch',
            name='dna_extraction',
            field=models.CharField(blank=True, max_length=3, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='batch',
            name='rna_extraction',
            field=models.CharField(blank=True, max_length=3, null=True, unique=True),
        ),
    ]