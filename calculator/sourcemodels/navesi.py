from django.db import models
from django.contrib import admin


class NavesidlinaZaboraAdmin(admin.ModelAdmin):
    list_display = (
        'start',
        'end',
        'price',
        'mnosh'
    )


class NavesidlinaZabora(models.Model):
    start = models.DecimalField("Начало промежутка", max_digits=100, decimal_places=0)
    end = models.DecimalField("Конец промежутка", max_digits=100, decimal_places=0)
    price = models.DecimalField("Прибавлять за каждый каждый метр", max_digits=100, decimal_places=2)
    mnosh = models.DecimalField("Умножить результат при выборе на", max_digits=100, decimal_places=5)

    class Meta:
        verbose_name = 'длину забора'
        verbose_name_plural = '[Navesi] Длина забора'



class NavesishirinaZaboraAdmin(admin.ModelAdmin):
    list_display = (
        'start',
        'end',
        'price',
        'mnosh'
    )


class NavesishirinaZabora(models.Model):
    start = models.DecimalField("Начало промежутка", max_digits=100, decimal_places=0)
    end = models.DecimalField("Конец промежутка", max_digits=100, decimal_places=0)
    price = models.DecimalField("Прибавлять за каждый каждый метр", max_digits=100, decimal_places=2)
    mnosh = models.DecimalField("Умножить результат при выборе на", max_digits=100, decimal_places=5)

    class Meta:
        verbose_name = 'Ширина забора'
        verbose_name_plural = '[Navesi] Ширина забора'



class NavesivisotaZaboraAdmin(admin.ModelAdmin):
    list_display = (
        'value',
        'mnosh',
        'price'
    )

class NavesivisotaZabora(models.Model):
    value = models.CharField("Значение поля", max_length=300)
    mnosh = models.DecimalField("Умножить результат при выборе на", max_digits=100, decimal_places=5)
    price = models.DecimalField("Прибавлять за каждый каждый метр", max_digits=100, decimal_places=2)
    class Meta:
        verbose_name = 'высоту забора'
        verbose_name_plural = '[Navesi] Высота забора'

class NavesitypAdmin(admin.ModelAdmin):
    list_display = (
        'value',
        'mnosh',
        'price'
    )

class Navesityp(models.Model):
    value = models.CharField("Значение поля", max_length=300)
    mnosh = models.DecimalField("Умножить результат при выборе на", max_digits=100, decimal_places=5)
    price = models.DecimalField("Прибавлять за каждый каждый метр", max_digits=100, decimal_places=2)
    class Meta:
        verbose_name = 'Тип фермы'
        verbose_name_plural = '[Navesi] Тип фермы'


class NavesirazmerAdmin(admin.ModelAdmin):
    list_display = (
        'value',
        'mnosh',
        'price'
    )

class Navesirazmer(models.Model):
    value = models.CharField("Значение поля", max_length=300)
    mnosh = models.DecimalField("Умножить результат при выборе на", max_digits=100, decimal_places=5)
    price = models.DecimalField("Прибавлять за каждый каждый метр", max_digits=100, decimal_places=2)
    class Meta:
        verbose_name = 'Размер и толщина столбцо'
        verbose_name_plural = '[Navesi] Размер и толщина столбцо'


class NavesimethodAdmin(admin.ModelAdmin):
    list_display = (
        'value',
        'mnosh',
        'price'
    )

class Navesimethod(models.Model):
    value = models.CharField("Значение поля", max_length=300)
    mnosh = models.DecimalField("Умножить результат при выборе на", max_digits=100, decimal_places=5)
    price = models.DecimalField("Прибавлять за каждый каждый метр", max_digits=100, decimal_places=2)
    class Meta:
        verbose_name = 'Метод установки столбов'
        verbose_name_plural = '[Navesi] Метод установки столбов'


class NavesikrovlyaAdmin(admin.ModelAdmin):
    list_display = (
        'value',
        'mnosh',
        'price'
    )

class Navesikrovlya(models.Model):
    value = models.CharField("Значение поля", max_length=300)
    mnosh = models.DecimalField("Умножить результат при выборе на", max_digits=100, decimal_places=5)
    price = models.DecimalField("Прибавлять за каждый каждый метр", max_digits=100, decimal_places=2)
    class Meta:
        verbose_name = 'Кровельный материал'
        verbose_name_plural = '[Navesi] Кровельный материал'


class NavesifermiAdmin(admin.ModelAdmin):
    list_display = (
        'value',
        'mnosh',
        'price'
    )

class Navesifermi(models.Model):
    value = models.CharField("Значение поля", max_length=300)
    mnosh = models.DecimalField("Умножить результат при выборе на", max_digits=100, decimal_places=5)
    price = models.DecimalField("Прибавлять за каждый каждый метр", max_digits=100, decimal_places=2)
    class Meta:
        verbose_name = 'Боковые фермы'
        verbose_name_plural = '[Navesi] Боковые фермы'


class NavesikmMkadAdmin(admin.ModelAdmin):
    list_display = (
        'start',
        'end',
        'price',
        'mnosh'
    )


class NavesikmMkad(models.Model):
    start = models.DecimalField("Начало промежутка", max_digits=100, decimal_places=0)
    end = models.DecimalField("Конец промежутка", max_digits=100, decimal_places=0)
    price = models.DecimalField("Прибавлять за каждый каждый метр", max_digits=100, decimal_places=2)
    mnosh = models.DecimalField("Умножить результат при выборе на", max_digits=100, decimal_places=5)

    class Meta:
        verbose_name = 'расстояние МКАД'
        verbose_name_plural = '[Navesi] Количество км от МКАД'
