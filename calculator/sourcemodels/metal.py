from django.db import models
from django.contrib import admin


class MetaldlinastolbovAdmin(admin.ModelAdmin):
    list_display = (
        'visota',
        'tolshina',
        'price',
    )


class Metaldlinastolbov(models.Model):
    visota = models.DecimalField("Высота столба", max_digits=100, decimal_places=2)
    tolshina = models.DecimalField("Толщина столба", max_digits=100, decimal_places=2)
    price = models.DecimalField("Цена конфигурации", max_digits=100, decimal_places=2)

    class Meta:
        verbose_name = '[Metal] Цена столбов'
        verbose_name_plural = verbose_name


class MetalshtaketnikAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'visota',
        'polymer',
        'price',
    )


class Metalshtaketnik(models.Model):
    title = models.CharField("Количество горизонталей (лаги)", max_length=100)
    visota = models.DecimalField("Высота столба", max_digits=100, decimal_places=2)
    polymer = models.CharField('Название полимера', max_length=100)
    price = models.DecimalField("Цена конфигурации", max_digits=100, decimal_places=2)

    class Meta:
        verbose_name = '[Metal] Штакетник'
        verbose_name_plural = verbose_name



class MetallagsAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'price',
        'count_mnsh'
    )


class Metallags(models.Model):
    title = models.CharField("Название штакетника", max_length=100)
    price = models.DecimalField("Цена конфигурации", max_digits=100, decimal_places=2)
    count_mnsh = models.DecimalField("Множитель количества", max_digits=100, decimal_places=2)

    class Meta:
        verbose_name = '[Metal] Лаги'
        verbose_name_plural = verbose_name





class MetalystanovkavorotAdmin(admin.ModelAdmin):
    list_display = (
        'price',
    )


class Metalystanovkavorot(models.Model):
    price = models.DecimalField("Цена за установку ворот", max_digits=100, decimal_places=2)

    class Meta:
        verbose_name = '[Metal] Цена за установку ворот'
        verbose_name_plural = verbose_name



class MetalystanovkazaboraAdmin(admin.ModelAdmin):
    list_display = (
        'start',
        'end',
        'price',
    )


class Metalystanovkazabora(models.Model):
    start = models.DecimalField("Начало промежутка", max_digits=100, decimal_places=2)
    end = models.DecimalField("Конец промежутка", max_digits=100, decimal_places=2)
    price = models.DecimalField("Цена за установку забора", max_digits=100, decimal_places=2)

    class Meta:
        verbose_name = '[Metal] Цена за установку забора'
        verbose_name_plural = verbose_name


class MetalvorotaAdmin(admin.ModelAdmin):
    list_display = (
        'visota',
        'shirina',
        'price',
    )


class Metalvorota(models.Model):
    visota = models.DecimalField("Высота", max_digits=100, decimal_places=2)
    shirina = models.DecimalField("Ширина", max_digits=100, decimal_places=2)
    price = models.DecimalField("Цена", max_digits=100, decimal_places=2)

    class Meta:
        verbose_name = '[Metal] Ворота'
        verbose_name_plural = verbose_name


class MetalkalitkaAdmin(admin.ModelAdmin):
    list_display = (
        'visota',
        'price',
    )


class Metalkalitka(models.Model):
    visota = models.DecimalField("Высота", max_digits=100, decimal_places=2)
    price = models.DecimalField("Цена", max_digits=100, decimal_places=2)

    class Meta:
        verbose_name = '[Metal] Калитка'
        verbose_name_plural = verbose_name


class MetalystanovkakalitkiAdmin(admin.ModelAdmin):
    list_display = (
        'price',
    )


class Metalystanovkakalitki(models.Model):
    price = models.DecimalField("Цена", max_digits=100, decimal_places=2)

    class Meta:
        verbose_name = '[Metal] Установка калитки'
        verbose_name_plural = verbose_name



class MetalpokraskaAdmin(admin.ModelAdmin):
    list_display = (
        'tip',
        'price',
        'kolvo',
    )


class Metalpokraska(models.Model):
    tip = models.CharField("Тип краски", max_length=100)
    price = models.DecimalField("Цена", max_digits=100, decimal_places=2)
    kolvo = models.DecimalField("Количество краски на метр", max_digits=100, decimal_places=5)

    class Meta:
        verbose_name = '[Metal] Покраска'
        verbose_name_plural = verbose_name


