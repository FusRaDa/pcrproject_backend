# Generated by Django 4.0.7 on 2022-10-21 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0047_remove_batch_assayname_alter_batch_assay'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assay',
            name='supply',
        ),
    ]