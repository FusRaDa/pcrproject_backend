# Generated by Django 4.0.7 on 2022-10-04 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_groupassay_alter_batch_assaycode'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupassay',
            name='assays',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.assay'),
        ),
    ]