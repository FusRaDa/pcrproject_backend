# Generated by Django 4.0.7 on 2022-11-09 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0065_alter_assay_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assay',
            name='type',
            field=models.CharField(choices=[('DNA', 'DNA'), ('RNA', 'RNA'), ('Total nucleic', 'Total nucleic')], default=None, max_length=15),
        ),
    ]
