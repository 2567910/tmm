# Generated by Django 3.2.9 on 2022-03-04 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translation_management_tool', '0026_alter_translationkey_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicaltranslation',
            name='value',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='translation',
            name='value',
            field=models.TextField(blank=True, default=''),
        ),
    ]