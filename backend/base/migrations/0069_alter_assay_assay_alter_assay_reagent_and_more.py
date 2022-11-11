# Generated by Django 4.0.7 on 2022-11-11 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0068_rename_assays_assay_assay'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assay',
            name='assay',
            field=models.ManyToManyField(blank=True, related_name='grouped_assays', to='base.assay'),
        ),
        migrations.AlterField(
            model_name='assay',
            name='reagent',
            field=models.ManyToManyField(blank=True, to='base.reagent'),
        ),
        migrations.AlterField(
            model_name='assay',
            name='supply',
            field=models.ManyToManyField(blank=True, to='base.supply'),
        ),
    ]