# Generated by Django 4.0.7 on 2022-10-04 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_alter_assay_code_alter_assay_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupAssay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, null=True)),
                ('code', models.CharField(max_length=25, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='batch',
            name='assayCode',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.groupassay'),
        ),
    ]
