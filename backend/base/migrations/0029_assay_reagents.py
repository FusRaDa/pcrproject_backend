# Generated by Django 4.0.7 on 2022-10-06 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0028_delete_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='assay',
            name='reagents',
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
    ]
