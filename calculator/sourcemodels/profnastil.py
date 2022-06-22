from django.db import models
from django.contrib import admin


class ProfnastildlinastolbovAdmin(admin.ModelAdmin):
    list_display = (
        'visota',
        'tolshina',
        'price',
    )


class Profnastildlinastolbov(models.Model):
    visota = models.DecimalField("Высота столба", max_digits=100, decimal_places=2)
    tolshina = models.DecimalField("Толщина столба", max_digits=100, decimal_places=2)
    price = models.DecimalField("Цена конфигурации", max_digits=100, decimal_places=2)

    class Meta:
        verbose_name = '[Profnastil] Цена столбов'
        verbose_name_plural = verbose_name


class ProfnastilshtaketnikAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'polymer',
        'price',
    )



class Profnastilshtaketnik(models.Model):
    title = models.CharField("Название штакетника", max_length=100)
    polymer = models.CharField('Название полимера', max_length=100)
    price = models.DecimalField("Цена конфигурации", max_digits=100, decimal_places=2)

    class Meta:
        verbose_name = '[Profnastil] Штакетник'
        verbose_name_plural = verbose_name



class ProfnastillagsAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'price',
        'count_mnsh'
    )


class Profnastillags(models.Model):
    title = models.CharField("Количество горизонталей (лаги)", max_length=100)
    price = models.DecimalField("Цена конфигурации", max_digits=100, decimal_places=2)
    count_mnsh = models.DecimalField("Множитель количества", max_digits=100, decimal_places=2)

    class Meta:
        verbose_name = '[Profnastil] Лаги'
        verbose_name_plural = verbose_name





class ProfnastilystanovkavorotAdmin(admin.ModelAdmin):
    list_display = (
        'price',
    )


class Profnastilystanovkavorot(models.Model):
    price = models.DecimalField("Цена за установку ворот", max_digits=100, decimal_places=2)

    class Meta:
        verbose_name = '[Profnastil] Цена за установку ворот'
        verbose_name_plural = verbose_name



class ProfnastilystanovkazaboraAdmin(admin.ModelAdmin):
    list_display = (
        'start',
        'end',
        'price',
    )


class Profnastilystanovkazabora(models.Model):
    start = models.DecimalField("Начало промежутка", max_digits=100, decimal_places=2)
    end = models.DecimalField("Конец промежутка", max_digits=100, decimal_places=2)
    price = models.DecimalField("Цена за установку забора", max_digits=100, decimal_places=2)

    class Meta:
        verbose_name = '[Profnastil] Цена за установку забора'
        verbose_name_plural = verbose_name


class ProfnastilvorotaAdmin(admin.ModelAdmin):
    list_display = (
        'visota',
        'shirina',
        'price',
    )


class Profnastilvorota(models.Model):
    visota = models.DecimalField("Высота", max_digits=100, decimal_places=2)
    shirina = models.DecimalField("Ширина", max_digits=100, decimal_places=2)
    price = models.DecimalField("Цена", max_digits=100, decimal_places=2)

    class Meta:
        verbose_name = '[Profnastil] Ворота'
        verbose_name_plural = verbose_name


class ProfnastilkalitkaAdmin(admin.ModelAdmin):
    list_display = (
        'visota',
        'price',
    )


class Profnastilkalitka(models.Model):
    visota = models.DecimalField("Высота", max_digits=100, decimal_places=2)
    price = models.DecimalField("Цена", max_digits=100, decimal_places=2)

    class Meta:
        verbose_name = '[Profnastil] Калитка'
        verbose_name_plural = verbose_name


class ProfnastilystanovkakalitkiAdmin(admin.ModelAdmin):
    list_display = (
        'price',
    )


class Profnastilystanovkakalitki(models.Model):
    price = models.DecimalField("Цена", max_digits=100, decimal_places=2)

    class Meta:
        verbose_name = '[Profnastil] Установка калитки'
        verbose_name_plural = verbose_name



class ProfnastilpokraskaAdmin(admin.ModelAdmin):
    list_display = (
        'tip',
        'price',
        'kolvo',
    )


class Profnastilpokraska(models.Model):
    tip = models.CharField("Тип краски", max_length=100)
    price = models.DecimalField("Цена", max_digits=100, decimal_places=2)
    kolvo = models.DecimalField("Количество краски на метр", max_digits=100, decimal_places=5)

    class Meta:
        verbose_name = '[Profnastil] Покраска'
        verbose_name_plural = verbose_name
