# Generated by Django 4.0.7 on 2022-10-04 21:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0020_alter_assay_code_alter_assay_groupassays'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assay',
            old_name='groupAssays',
            new_name='group',
        ),
    ]