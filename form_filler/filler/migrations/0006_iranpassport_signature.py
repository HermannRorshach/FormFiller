# Generated by Django 4.2 on 2024-06-22 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filler', '0005_iranpassport_issuing_authority'),
    ]

    operations = [
        migrations.AddField(
            model_name='iranpassport',
            name='signature',
            field=models.CharField(choices=[('empty', '-'), ('signature', '/подпись/')], default='empty', max_length=9, verbose_name='Подпись'),
        ),
    ]