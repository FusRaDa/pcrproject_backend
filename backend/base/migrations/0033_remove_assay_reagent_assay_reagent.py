# Generated by Django 4.0.7 on 2022-10-06 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0032_reagent_supply_rename_reagents_assay_reagent_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assay',
            name='reagent',
        ),
        migrations.AddField(
            model_name='assay',
            name='reagent',
            field=models.ManyToManyField(to='base.reagent'),
        ),
    ]