# Generated by Django 4.2 on 2024-07-04 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filler', '0007_template'),
    ]

    operations = [
        migrations.RenameField(
            model_name='template',
            old_name='row_fields',
            new_name='raw_fields',
        ),
    ]
