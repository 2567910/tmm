# Generated by Django 3.2.9 on 2022-03-24 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('translation_management_tool', '0032_auto_20220316_2205'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='translationkey',
            unique_together={('key', 'project')},
        ),
    ]
