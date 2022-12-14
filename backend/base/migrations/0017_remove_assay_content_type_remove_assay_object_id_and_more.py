# Generated by Django 4.0.7 on 2022-10-04 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_remove_batch_assaycode_assay_content_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assay',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='assay',
            name='object_id',
        ),
        migrations.RemoveField(
            model_name='batch',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='batch',
            name='object_id',
        ),
        migrations.AddField(
            model_name='batch',
            name='groupAssay',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.groupassay'),
        ),
        migrations.AddField(
            model_name='batch',
            name='singleAssay',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.assay'),
        ),
        migrations.AlterField(
            model_name='groupassay',
            name='assays',
            field=models.ManyToManyField(to='base.assay'),
        ),
    ]
