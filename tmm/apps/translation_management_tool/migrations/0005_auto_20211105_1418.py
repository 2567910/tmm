# Generated by Django 3.1.7 on 2021-11-05 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translation_management_tool', '0004_auto_20211105_1413'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='language',
            options={'ordering': ['languages']},
        ),
        migrations.RenameField(
            model_name='language',
            old_name='language',
            new_name='languages',
        ),
        migrations.AlterField(
            model_name='project',
            name='languagees',
            field=models.ManyToManyField(related_name='project', to='translation_management_tool.Language'),
        ),
    ]
