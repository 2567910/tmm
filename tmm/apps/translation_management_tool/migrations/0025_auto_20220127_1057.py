# Generated by Django 3.2.9 on 2022-01-27 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translation_management_tool', '0024_auto_20220113_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicaltranslation',
            name='value',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='translation',
            name='value',
            field=models.TextField(blank=True, null=True),
        ),
    ]
