from django.db import models


class IranPassport(models.Model):
    SEX_CHOICES = [
        ("M", "мужской"),
        ("F", "женский"),
    ]
    passport_number = models.CharField(
        max_length=9, verbose_name='Номер паспорта')
    surname = models.CharField(max_length=30, verbose_name='Фамилия')
    name = models.CharField(max_length=30, verbose_name='Имя')
    father_name = models.CharField(max_length=30, verbose_name='Имя отца')
    birthday = models.CharField(max_length=30, verbose_name='Дата рождения')
    place_of_birthday = models.CharField(
        max_length=30, verbose_name='Место рождения')
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, default='M', verbose_name='Пол')
    date_of_issue = models.CharField(max_length=30, verbose_name='Дата выдачи')
    date_of_expiry = models.CharField(
        max_length=30, verbose_name='Действителен до')
    lond_number = models.CharField(max_length=30, verbose_name='Длинный номер')

    def __str__(self):
        return f"Иран пасп. {self.surname} {self.name}"
