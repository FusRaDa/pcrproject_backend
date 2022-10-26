# Generated by Django 4.0.7 on 2022-10-26 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0056_alter_batch_dna_extraction_and_more'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='batch',
            constraint=models.UniqueConstraint(fields=('dna_extraction', 'rna_extraction'), name='extraction_groups'),
        ),
    ]
