# Generated by Django 4.0.7 on 2022-10-21 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0048_remove_assay_supply'),
    ]

    operations = [
        migrations.AddField(
            model_name='assay',
            name='type',
            field=models.CharField(choices=[('DNA', 'DNA'), ('RNA', 'RNA'), ('Total nucleic', 'Total nucleic')], default='DNA', max_length=15),
        ),
    ]
