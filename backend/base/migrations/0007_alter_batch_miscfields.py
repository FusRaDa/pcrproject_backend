# Generated by Django 4.0.7 on 2022-10-04 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_batch_miscfields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='miscFields',
            field=models.JSONField(),
        ),
    ]
