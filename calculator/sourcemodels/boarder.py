from django.db import models
from django.contrib import admin


class BoarderdlinaZaboraAdmin(admin.ModelAdmin):
    list_display = (
        'start',
        'end',
        'price',
        'mnosh'
    )


class BoarderdlinaZabora(models.Model):
    start = models.DecimalField("Начало промежутка", max_digits=100, decimal_places=0)
    end = models.DecimalField("Конец промежутка", max_digits=100, decimal_places=0)
    price = models.DecimalField("Прибавлять за каждый каждый метр", max_digits=100, decimal_places=2)
    mnosh = models.DecimalField("Умножить результат при выборе на", max_digits=100, decimal_places=5)

    class Meta:
        verbose_name = 'длину забора'
        verbose_name_plural = '[Boarder] Длина забора'


class BoardervisotaZaboraAdmin(admin.ModelAdmin):
    list_display = (
        'value',
        'mnosh',
        'price'
    )


class BoardervisotaZabora(models.Model):
    value = models.CharField("Значение поля", max_length=300)
    mnosh = models.DecimalField("Умножить результат при выборе на", max_digits=100, decimal_places=5)
    price = models.DecimalField("Прибавлять за каждый каждый метр", max_digits=100, decimal_places=2)
    class Meta:
        verbose_name = 'высоту забора'
        verbose_name_plural = '[Boarder] Высота забора'

class BoarderpaneliAdmin(admin.ModelAdmin):
    list_display = (
        'value',
        'mnosh',
        'price'
    )


class Boarderpaneli(models.Model):
    value = models.CharField("Значение поля", max_length=300)
    mnosh = models.DecimalField("Умножить результат при выборе на", max_digits=100, decimal_places=5)
    price = models.DecimalField("Прибавлять за каждый каждый метр", max_digits=100, decimal_places=2)
    class Meta:
        verbose_name = 'Панели 3D (ячейка 200*55 мм)'
        verbose_name_plural = '[Boarder] Панели 3D (ячейка 200*55 мм)'

class BoarderrazmerAdmin(admin.ModelAdmin):
    list_display = (
        'value',
        'mnosh',
        'price'
    )


class Boarderrazmer(models.Model):
    value = models.CharField("Значение поля", max_length=300)
    mnosh = models.DecimalField("Умножить результат при выборе на", max_digits=100, decimal_places=5)
    price = models.DecimalField("Прибавлять за каждый каждый метр", max_digits=100, decimal_places=2)
    class Meta:
        verbose_name = 'Размер столбов, мм'
        verbose_name_plural = '[Boarder] Размер столбов, мм'

class BoardermethodstandAdmin(admin.ModelAdmin):
    list_display = (
        'value',
        'mnosh',
        'price'
    )


class Boardermethodstand(models.Model):
    value = models.CharField("Значение поля", max_length=300)
    mnosh = models.DecimalField("Умножить результат при выборе на", max_digits=100, decimal_places=5)
    price = models.DecimalField("Прибавлять за каждый каждый метр", max_digits=100, decimal_places=2)
    class Meta:
        verbose_name = 'Покрытие столбов'
        verbose_name_plural = '[Boarder] Покрытие столбов'

class BoarderkalitkaStandartAdmin(admin.ModelAdmin):
    list_display = (
        'value',
        'mnosh',
        'price'
    )


class BoarderkalitkaStandart(models.Model):
    value = models.CharField("Значение поля", max_length=300)
    mnosh = models.DecimalField("Умножить результат при выборе на", max_digits=100, decimal_places=5)
    price = models.DecimalField("Прибавлять за каждый каждый метр", max_digits=100, decimal_places=2)
    class Meta:
        verbose_name = 'Калитка Стандарт'
        verbose_name_plural = '[Boarder] Калитка Стандарт'

class BoarderraspashvorotaAdmin(admin.ModelAdmin):
    list_display = (
        'value',
        'mnosh',
        'price'
    )


class Boarderraspashvorota(models.Model):
    value = models.CharField("Значение поля", max_length=300)
    mnosh = models.DecimalField("Умножить результат при выборе на", max_digits=100, decimal_places=5)
    price = models.DecimalField("Прибавлять за каждый каждый метр", max_digits=100, decimal_places=2)
    class Meta:
        verbose_name = 'Распашные ворота'
        verbose_name_plural = '[Boarder] Распашные ворота'

class BoarderotkatAdmin(admin.ModelAdmin):
    list_display = (
        'value',
        'mnosh',
        'price'
    )


class Boarderotkat(models.Model):
    value = models.CharField("Значение поля", max_length=300)
    mnosh = models.DecimalField("Умножить результат при выборе на", max_digits=100, decimal_places=5)
    price = models.DecimalField("Прибавлять за каждый каждый метр", max_digits=100, decimal_places=2)
    class Meta:
        verbose_name = 'Откатные (сдвижные) ворота'
        verbose_name_plural = '[Boarder] Откатные (сдвижные) ворота'

class BoarderdemontashAdmin(admin.ModelAdmin):
    list_display = (
        'value',
        'mnosh',
        'price'
    )


class Boarderdemontash(models.Model):
    value = models.CharField("Значение поля", max_length=300)
    mnosh = models.DecimalField("Умножить результат при выборе на", max_digits=100, decimal_places=5)
    price = models.DecimalField("Прибавлять за каждый каждый метр", max_digits=100, decimal_places=2)
    class Meta:
        verbose_name = 'Демонтаж старого забора'
        verbose_name_plural = '[Boarder] Демонтаж старого забора'


class BoarderkmMkadAdmin(admin.ModelAdmin):
    list_display = (
        'start',
        'end',
        'price',
        'mnosh'
    )


class BoarderkmMkad(models.Model):
    start = models.DecimalField("Начало промежутка", max_digits=100, decimal_places=0)
    end = models.DecimalField("Конец промежутка", max_digits=100, decimal_places=0)
    price = models.DecimalField("Прибавлять за каждый каждый метр", max_digits=100, decimal_places=2)
    mnosh = models.DecimalField("Умножить результат при выборе на", max_digits=100, decimal_places=5)

    class Meta:
        verbose_name = 'расстояние МКАД'
        verbose_name_plural = '[Boarder] Количество км от МКАД'
