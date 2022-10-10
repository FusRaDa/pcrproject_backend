# Generated by Django 4.0.7 on 2022-10-06 23:35

import base.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0031_alter_assay_reagents_alter_batch_miscfields'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reagent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, null=True, unique=True)),
                ('catalogNumber', models.CharField(max_length=25, null=True, unique=True)),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=7, validators=[base.models.validate_nonzero])),
            ],
        ),
        migrations.CreateModel(
            name='Supply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, null=True, unique=True)),
                ('catalogNumber', models.CharField(max_length=25, null=True, unique=True)),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=7, validators=[base.models.validate_nonzero])),
            ],
        ),
        migrations.RenameField(
            model_name='assay',
            old_name='reagents',
            new_name='reagent',
        ),
        migrations.AddField(
            model_name='assay',
            name='supply',
            field=models.ManyToManyField(to='base.supply'),
        ),
    ]