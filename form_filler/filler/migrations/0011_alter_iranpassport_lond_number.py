# Generated by Django 5.1.2 on 2025-03-07 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filler', '0010_alter_iranpassport_birthday_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iranpassport',
            name='lond_number',
            field=models.CharField(max_length=27, verbose_name='Длинный номер'),
        ),
    ]
