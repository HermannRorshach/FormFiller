# Generated by Django 5.1.2 on 2025-03-07 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filler', '0009_alter_iranpassport_issuing_authority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iranpassport',
            name='birthday',
            field=models.CharField(max_length=8, verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='iranpassport',
            name='date_of_expiry',
            field=models.CharField(max_length=8, verbose_name='Действителен до'),
        ),
        migrations.AlterField(
            model_name='iranpassport',
            name='date_of_issue',
            field=models.CharField(max_length=8, verbose_name='Дата выдачи'),
        ),
        migrations.AlterField(
            model_name='iranpassport',
            name='issuing_authority',
            field=models.CharField(choices=[('authority1', 'Полковник\nОмид Нодехи'), ('authority2', 'Бригадный генерал\nАли Золгадри'), ('authority3', 'Бригадный генерал\nСадэг Резадуст'), ('authority4', 'Бригадный генерал\nМохаммад Бабаэи')], default='authority1', max_length=10, verbose_name='Имя и должность должностного лица'),
        ),
    ]
