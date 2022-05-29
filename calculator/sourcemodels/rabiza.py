from django.db import models
from django.contrib import admin


class RabizadlinastolbovAdmin(admin.ModelAdmin):
    list_display = (
        'visota',
        'tolshina',
        'price',
    )


class Rabizadlinastolbov(models.Model):
    visota = models.DecimalField("Высота столба", max_digits=100, decimal_places=2)
    tolshina = models.DecimalField("Толщина столба", max_digits=100, decimal_places=2)
    price = models.DecimalField("Цена конфигурации", max_digits=100, decimal_places=2)

    class Meta:
        verbose_name = '[Rabiza] Цена столбов'
        verbose_name_plural = verbose_name


class RabizasetkaAdmin(admin.ModelAdmin):
    list_display = (
        'tolshina',
        'visota',
        'price'
    )


class Rabizasetka(models.Model):
    tolshina = models.DecimalField("Толщина сетки", max_digits=100, decimal_places=2)
    visota = models.DecimalField("Высота забора", max_digits=100, decimal_places=2)
    price = models.DecimalField("Цена", max_digits=100, decimal_places=2)

    class Meta:
        verbose_name = '[Rabiza] Сетка'
        verbose_name_plural = verbose_name


class RabizaystanovkavorotAdmin(admin.ModelAdmin):
    list_display = (
        'price',
    )


class Rabizaystanovkavorot(models.Model):
    price = models.DecimalField("Цена за установку ворот", max_digits=100, decimal_places=2)

    class Meta:
        verbose_name = '[Rabiza] Цена за установку ворот'
        verbose_name_plural = verbose_name



class RabizaystanovkazaboraAdmin(admin.ModelAdmin):
    list_display = (
        'start',
        'end',
        'price',
    )


class Rabizaystanovkazabora(models.Model):
    start = models.DecimalField("Начало промежутка", max_digits=100, decimal_places=2)
    end = models.DecimalField("Конец промежутка", max_digits=100, decimal_places=2)
    price = models.DecimalField("Цена за установку забора", max_digits=100, decimal_places=2)

    class Meta:
        verbose_name = '[Rabiza] Цена за установку забора'
        verbose_name_plural = verbose_name


class RabizavorotaAdmin(admin.ModelAdmin):
    list_display = (
        'visota',
        'shirina',
        'price',
    )


class Rabizavorota(models.Model):
    visota = models.DecimalField("Высота", max_digits=100, decimal_places=2)
    shirina = models.DecimalField("Ширина", max_digits=100, decimal_places=2)
    price = models.DecimalField("Цена", max_digits=100, decimal_places=2)

    class Meta:
        verbose_name = '[Rabiza] Ворота'
        verbose_name_plural = verbose_name


class RabizakalitkaAdmin(admin.ModelAdmin):
    list_display = (
        'visota',
        'price',
    )


class Rabizakalitka(models.Model):
    visota = models.DecimalField("Высота", max_digits=100, decimal_places=2)
    price = models.DecimalField("Цена", max_digits=100, decimal_places=2)

    class Meta:
        verbose_name = '[Rabiza] Калитка'
        verbose_name_plural = verbose_name


class RabizaystanovkakalitkiAdmin(admin.ModelAdmin):
    list_display = (
        'price',
    )


class Rabizaystanovkakalitki(models.Model):
    price = models.DecimalField("Цена", max_digits=100, decimal_places=2)

    class Meta:
        verbose_name = '[Rabiza] Установка калитки'
        verbose_name_plural = verbose_name



class RabizapokraskaAdmin(admin.ModelAdmin):
    list_display = (
        'tip',
        'price',
        'kolvo',
    )


class Rabizapokraska(models.Model):
    tip = models.CharField("Тип краски", max_length=100)
    price = models.DecimalField("Цена", max_digits=100, decimal_places=2)
    kolvo = models.DecimalField("Количество краски на метр", max_digits=100, decimal_places=5)

    class Meta:
        verbose_name = '[Rabiza] Покраска'
        verbose_name_plural = verbose_name


class RabizaarmaturaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'price',
    )


class Rabizaarmatura(models.Model):
    price = models.DecimalField("Цена", max_digits=100, decimal_places=2)

    class Meta:
        verbose_name = '[Rabiza] Арматура'
        verbose_name_plural = verbose_name
