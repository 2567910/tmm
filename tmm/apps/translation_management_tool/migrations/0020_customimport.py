# Generated by Django 3.2.9 on 2022-01-06 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translation_management_tool', '0019_alter_translationkey_unique_together'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomImport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(db_index=True, max_length=255, unique=True)),
            ],
        ),
    ]
