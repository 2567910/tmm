# Generated by Django 3.2.9 on 2022-01-13 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translation_management_tool', '0023_auto_20220111_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='translationkey',
            name='key',
            field=models.CharField(help_text="<p>For more information about the i18next value options <a href='https://www.i18next.com/misc/json-format' target='_blank'>click here</a>.</p>", max_length=255),
        ),
        migrations.AlterUniqueTogether(
            name='translationkey',
            unique_together=set(),
        ),
    ]
