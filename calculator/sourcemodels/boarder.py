from django.db import models
from django.contrib import admin


class BoarderdlinastolbovAdmin(admin.ModelAdmin):
    list_display = (
        'visota',
        'tolshina',
        'price',
    )


class Boarderdlinastolbov(models.Model):
    visota = models.DecimalField("Высота столба", max_digits=100, decimal_places=2)
    tolshina = models.DecimalField("Толщина столба", max_digits=100, decimal_places=2)
    price = models.DecimalField("Цена конфигурации", max_digits=100, decimal_places=2)

    class Meta:
        verbose_name = '[Boarder] Цена столбов'
        verbose_name_plural = verbose_name


class BoarderystanovkavorotAdmin(admin.ModelAdmin):
    list_display = (
        'price',
    )


class Boarderystanovkavorot(models.Model):
    price = models.DecimalField("Цена за установку ворот", max_digits=100, decimal_places=2)

    class Meta:
        verbose_name = '[Boarder] Цена за установку ворот'
        verbose_name_plural = verbose_name



class BoarderystanovkazaboraAdmin(admin.ModelAdmin):
    list_display = (
        'start',
        'end',
        'price',
    )


class Boarderystanovkazabora(models.Model):
    start = models.DecimalField("Начало промежутка", max_digits=100, decimal_places=2)
    end = models.DecimalField("Конец промежутка", max_digits=100, decimal_places=2)
    price = models.DecimalField("Цена за установку забора", max_digits=100, decimal_places=2)

    class Meta:
        verbose_name = '[Boarder] Цена за установку забора'
        verbose_name_plural = verbose_name


class BoardervorotaAdmin(admin.ModelAdmin):
    list_display = (
        'visota',
        'shirina',
        'price',
    )


class Boardervorota(models.Model):
    visota = models.DecimalField("Высота", max_digits=100, decimal_places=2)
    shirina = models.DecimalField("Ширина", max_digits=100, decimal_places=2)
    price = models.DecimalField("Цена", max_digits=100, decimal_places=2)

    class Meta:
        verbose_name = '[Boarder] Ворота'
        verbose_name_plural = verbose_name


class BoarderkalitkaAdmin(admin.ModelAdmin):
    list_display = (
        'visota',
        'price',
    )


class Boarderkalitka(models.Model):
    visota = models.DecimalField("Высота", max_digits=100, decimal_places=2)
    price = models.DecimalField("Цена", max_digits=100, decimal_places=2)

    class Meta:
        verbose_name = '[Boarder] Калитка'
        verbose_name_plural = verbose_name


class BoarderystanovkakalitkiAdmin(admin.ModelAdmin):
    list_display = (
        'price',
    )


class Boarderystanovkakalitki(models.Model):
    price = models.DecimalField("Цена", max_digits=100, decimal_places=2)

    class Meta:
        verbose_name = '[Boarder] Установка калитки'
        verbose_name_plural = verbose_name



class BoarderpokraskaAdmin(admin.ModelAdmin):
    list_display = (
        'tip',
        'price',
        'kolvo',
    )


class Boarderpokraska(models.Model):
    tip = models.CharField("Тип краски", max_length=100)
    price = models.DecimalField("Цена", max_digits=100, decimal_places=2)
    kolvo = models.DecimalField("Количество краски на метр", max_digits=100, decimal_places=5)

    class Meta:
        verbose_name = '[Boarder] Покраска'
        verbose_name_plural = verbose_name

