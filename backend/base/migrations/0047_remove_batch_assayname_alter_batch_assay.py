# Generated by Django 4.0.7 on 2022-10-17 20:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0046_batch_assayname_alter_batch_assay'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='batch',
            name='assayName',
        ),
        migrations.AlterField(
            model_name='batch',
            name='assay',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.assay'),
        ),
    ]