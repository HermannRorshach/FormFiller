from django.contrib.auth import get_user_model
from django.db import models


class IranPassport(models.Model):
    SEX_CHOICES = [
        ("M", "мужской"),
        ("F", "женский"),
    ]
    ISSUING_AUTHORITY_CHOICES = [
        ("authority1", "Полковник\nОмид Нодехи"),
        ("authority2", "Бригадный генерал\nАли Золгадри"),
        ("authority3", "Бригадный генерал\nСадэг Резадуст"),
        ("authority4", "Бригадный генерал\nМохаммад Бабаэи"),
    ]
    SIGNATURE_CHOICES = [
        ("empty", "-"),
        ("signature", "/подпись/"),
    ]

    passport_number = models.CharField(
        max_length=9, verbose_name='Номер паспорта')
    surname = models.CharField(max_length=30, verbose_name='Фамилия')
    name = models.CharField(max_length=30, verbose_name='Имя')
    father_name = models.CharField(max_length=30, verbose_name='Имя отца')
    birthday = models.CharField(max_length=8, verbose_name='Дата рождения')
    place_of_birthday = models.CharField(
        max_length=30, verbose_name='Место рождения')
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, default='M', verbose_name='Пол')
    date_of_issue = models.CharField(max_length=8, verbose_name='Дата выдачи')
    date_of_expiry = models.CharField(
        max_length=8, verbose_name='Действителен до')
    lond_number = models.CharField(max_length=27, verbose_name='Длинный номер')
    issuing_authority = models.CharField(
        max_length=10, choices=ISSUING_AUTHORITY_CHOICES,
        default='authority1',
        verbose_name='Имя и должность должностного лица')
    signature = models.CharField(
        max_length=9, choices=SIGNATURE_CHOICES,
        default='empty',
        verbose_name='Подпись')
    image = models.ImageField(
        verbose_name='Картинка',
        upload_to='%Y/%m/%d/',
        blank=True,
    )

    def __str__(self):
        return f"Иран пасп. {self.surname.upper()} {self.name.upper()}"


class Template(models.Model):
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='templates'
    )
    name = models.CharField(max_length=255)
    file_data = models.BinaryField()
    raw_fields = models.JSONField(default=list)
    fields = models.JSONField(default=dict)

    def __str__(self):
        return self.name
