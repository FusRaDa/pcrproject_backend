# Generated by Django 4.0.7 on 2022-11-03 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0062_alter_assay_reagent_alter_assay_supply'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assay',
            old_name='group',
            new_name='assays',
        ),
    ]
