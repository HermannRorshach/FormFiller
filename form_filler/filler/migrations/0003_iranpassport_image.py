# Generated by Django 4.2 on 2024-06-21 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filler', '0002_alter_iranpassport_sex'),
    ]

    operations = [
        migrations.AddField(
            model_name='iranpassport',
            name='image',
            field=models.ImageField(blank=True, upload_to='posts/%Y/%m/%d/', verbose_name='Картинка'),
        ),
    ]