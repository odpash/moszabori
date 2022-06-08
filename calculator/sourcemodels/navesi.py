from django.contrib import admin
from django.db import models


class NavesidlinastolbovAdmin(admin.ModelAdmin):
    list_display = (
        'visota',
        'tolshina',
        'price',
    )


class Navesidlinastolbov(models.Model):
    visota = models.DecimalField("Высота столба", max_digits=100, decimal_places=2)
    tolshina = models.CharField("Толщина столба", max_length=100)
    price = models.DecimalField("Цена конфигурации", max_digits=100, decimal_places=2)

    class Meta:
        verbose_name = '[Navesi] Цена столбов'
        verbose_name_plural = verbose_name


class NavesibalkaAdmin(admin.ModelAdmin):
    list_display = (
        'tolshina',
        'price',
    )


class Navesibalka(models.Model):
    tolshina = models.CharField("Толщина столба", max_length=100)
    price = models.DecimalField("Цена конфигурации", max_digits=100, decimal_places=2)

    class Meta:
        verbose_name = '[Navesi] Цена балки'
        verbose_name_plural = verbose_name


class NavesifermiAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
    )


class Navesifermi(models.Model):
    name = models.CharField("Введите название", max_length=100)
    price = models.DecimalField("Цена конфигурации", max_digits=100, decimal_places=2)

    class Meta:
        verbose_name = '[Navesi] Цена ферм'
        verbose_name_plural = verbose_name


class NavesiobrfermiAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
    )


class Navesiobrfermi(models.Model):
    name = models.CharField("Введите название", max_length=100)
    price = models.DecimalField("Цена конфигурации", max_digits=100, decimal_places=2)

    class Meta:
        verbose_name = '[Navesi] Обрешетка ферм'
        verbose_name_plural = verbose_name


class NavesikrovAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
    )


class Navesikrov(models.Model):
    name = models.CharField("Введите название", max_length=100)
    price = models.DecimalField("Цена конфигурации", max_digits=100, decimal_places=2)

    class Meta:
        verbose_name = '[Navesi] Кровельный материал'
        verbose_name_plural = verbose_name


class NavesikonekAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
    )


class Navesikonek(models.Model):
    name = models.CharField("Введите название", max_length=100)
    price = models.DecimalField("Цена конфигурации", max_digits=100, decimal_places=2)

    class Meta:
        verbose_name = '[Navesi] Конек'
        verbose_name_plural = verbose_name


class NavesibokfermaAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
    )


class Navesibokferma(models.Model):
    name = models.CharField("Введите название", max_length=100)
    price = models.DecimalField("Цена конфигурации", max_digits=100, decimal_places=2)

    class Meta:
        verbose_name = '[Navesi] Боковая ферма'
        verbose_name_plural = verbose_name


class NavesiveterAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
    )


class Navesiveter(models.Model):
    name = models.CharField("Введите название", max_length=100)
    price = models.DecimalField("Цена конфигурации", max_digits=100, decimal_places=2)

    class Meta:
        verbose_name = '[Navesi] Ветровая планка'
        verbose_name_plural = verbose_name


class NavesikraskaAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
    )


class Navesikraska(models.Model):
    name = models.CharField("Введите название", max_length=100)
    price = models.DecimalField("Цена конфигурации", max_digits=100, decimal_places=2)

    class Meta:
        verbose_name = '[Navesi] Краска'
        verbose_name_plural = verbose_name


class NavesiystanovkaAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
    )


class Navesiystanovka(models.Model):
    name = models.CharField("Введите название", max_length=100)
    price = models.DecimalField("Цена конфигурации", max_digits=100, decimal_places=2)

    class Meta:
        verbose_name = '[Navesi] Установка'
        verbose_name_plural = verbose_name
