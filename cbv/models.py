from django.db import models
from django.contrib.auth.models import User


from .translater import city_name_to_eng
from .translater import prof_name_to_eng
from .translater import comp_name_to_eng


class City(models.Model):
    name = models.CharField(max_length=15, blank=False, verbose_name='Город')
    slug = models.CharField(max_length=15, blank=True)

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Список городов'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = city_name_to_eng(self.name)
        super().save(*args, **kwargs)


class Profesion(models.Model):
    name = models.CharField(max_length=50, verbose_name='Специальность', unique=True)
    slug = models.CharField(max_length=50, blank=True, unique=True)

    class Meta:
        verbose_name = 'Специальность'
        verbose_name_plural = 'Специальности'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = prof_name_to_eng(self.name)
        super().save(*args, **kwargs)


class Company(models.Model):
    name = models.CharField(max_length=50, verbose_name='Работодатель', unique=True)
    slug = models.CharField(max_length=50, blank=True, unique=True)

    class Meta:
        verbose_name = 'Работодатель'
        verbose_name_plural = 'Работодатели'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = comp_name_to_eng(self.name)
        super().save(*args, **kwargs)


class Vacancy(models.Model):
    url = models.URLField(unique=True)
    title = models.CharField(max_length=200, verbose_name='Заголовок вакансии')
    description = models.TextField(verbose_name='Описание вакансии')
    city = models.ForeignKey('City', on_delete=models.CASCADE, verbose_name='Город')
    profesion = models.ForeignKey('Profesion', on_delete=models.CASCADE, verbose_name='Специальность')
    company = models.ManyToManyField('Company', verbose_name='Работодатель')
    timestamp = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

    def __str__(self):
        return self.title


class CompanyProfile(models.Model):
    company = models.OneToOneField("Company", on_delete=models.CASCADE)
    about = models.TextField(max_length=300)

    def __str__(self):
        return f"{self.company.name}Profile"
