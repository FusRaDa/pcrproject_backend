# Generated by Django 4.0.7 on 2022-10-07 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0035_alter_assay_reagent_alter_assay_supply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assay',
            name='reagent',
            field=models.ManyToManyField(to='base.reagent'),
        ),
        migrations.AlterField(
            model_name='assay',
            name='supply',
            field=models.ManyToManyField(to='base.supply'),
        ),
    ]
