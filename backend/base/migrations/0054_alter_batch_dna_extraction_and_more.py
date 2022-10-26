# Generated by Django 4.0.7 on 2022-10-26 00:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0053_extractiongroup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='dna_extraction',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dna_group', to='base.extractiongroup'),
        ),
        migrations.AlterField(
            model_name='batch',
            name='rna_extraction',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rna_group', to='base.extractiongroup'),
        ),
    ]
