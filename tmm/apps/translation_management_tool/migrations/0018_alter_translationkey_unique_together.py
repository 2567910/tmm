# Generated by Django 3.2.9 on 2021-12-15 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('translation_management_tool', '0017_historicaltranslation'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='translationkey',
            unique_together=set(),
        ),
    ]
