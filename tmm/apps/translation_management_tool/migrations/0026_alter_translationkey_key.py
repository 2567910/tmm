# Generated by Django 3.2.9 on 2022-03-04 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translation_management_tool', '0025_auto_20220127_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='translationkey',
            name='key',
            field=models.CharField(help_text="<p>v1.0.0 - For more information about the i18next value options <a href='https://www.i18next.com/misc/json-format' target='_blank'>click here</a>.</p>", max_length=255),
        ),
    ]