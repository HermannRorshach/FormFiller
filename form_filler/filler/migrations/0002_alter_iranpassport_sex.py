# Generated by Django 4.2 on 2024-05-25 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filler', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iranpassport',
            name='sex',
            field=models.CharField(choices=[('M', 'мужской'), ('F', 'женский')], default='M', max_length=1, verbose_name='Пол'),
        ),
    ]