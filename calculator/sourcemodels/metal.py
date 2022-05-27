from django.db import models
from django.contrib import admin


class MetaldlinaZaboraAdmin(admin.ModelAdmin):
    list_display = (
        'start',
        'end',
        'price',
        'mnosh'
    )


class MetaldlinaZabora(models.Model):
    start = models.DecimalField("Начало промежутка", max_digits=100, decimal_places=0)
    end = models.DecimalField("Конец промежутка", max_digits=100, decimal_places=0)
    price = models.DecimalField("Прибавлять за каждый каждый метр", max_digits=100, decimal_places=2)
    mnosh = models.DecimalField("Умножить результат при выборе на", max_digits=100, decimal_places=5)

    class Meta:
        verbose_name = 'длину забора'
        verbose_name_plural = '[Metal] Длина забора'


class MetalvisotaZaboraAdmin(admin.ModelAdmin):
    list_display = (
        'value',
        'mnosh',
        'price'
    )

class MetalvisotaZabora(models.Model):
    value = models.CharField("Значение поля", max_length=300)
    mnosh = models.DecimalField("Умножить результат при выборе на", max_digits=100, decimal_places=5)
    price = models.DecimalField("Прибавлять за каждый каждый метр", max_digits=100, decimal_places=2)
    class Meta:
        verbose_name = 'высоту забора'
        verbose_name_plural = '[Metal] Высота забора'


class MetaltipshtaketnikAdmin(admin.ModelAdmin):
    list_display = (
        'value',
        'mnosh',
        'price'
    )

class Metaltipshtaketnik(models.Model):
    value = models.CharField("Значение поля", max_length=300)
    mnosh = models.DecimalField("Умножить результат при выборе на", max_digits=100, decimal_places=5)
    price = models.DecimalField("Прибавлять за каждый каждый метр", max_digits=100, decimal_places=2)
    class Meta:
        verbose_name = 'Штакетник'
        verbose_name_plural = '[Metal] Штакетник'


class MetalkreplenieshtaketnikAdmin(admin.ModelAdmin):
    list_display = (
        'value',
        'mnosh',
        'price'
    )

class Metalkreplenieshtaketnik(models.Model):
    value = models.CharField("Значение поля", max_length=300)
    mnosh = models.DecimalField("Умножить результат при выборе на", max_digits=100, decimal_places=5)
    price = models.DecimalField("Прибавлять за каждый каждый метр", max_digits=100, decimal_places=2)
    class Meta:
        verbose_name = 'Крепление'
        verbose_name_plural = '[Metal] Крепление'


class MetalzazorAdmin(admin.ModelAdmin):
    list_display = (
        'value',
        'mnosh',
        'price'
    )

class Metalzazor(models.Model):
    value = models.CharField("Значение поля", max_length=300)
    mnosh = models.DecimalField("Умножить результат при выборе на", max_digits=100, decimal_places=5)
    price = models.DecimalField("Прибавлять за каждый каждый метр", max_digits=100, decimal_places=2)
    class Meta:
        verbose_name = 'Зазор'
        verbose_name_plural = '[Metal] Зазор'


class MetalpokritiestaketnikAdmin(admin.ModelAdmin):
    list_display = (
        'value',
        'mnosh',
        'price'
    )

class Metalpokritiestaketnik(models.Model):
    value = models.CharField("Значение поля", max_length=300)
    mnosh = models.DecimalField("Умножить результат при выборе на", max_digits=100, decimal_places=5)
    price = models.DecimalField("Прибавлять за каждый каждый метр", max_digits=100, decimal_places=2)
    class Meta:
        verbose_name = 'Покрытие'
        verbose_name_plural = '[Metal] Покрытие'


class MetalkolvoryadlagAdmin(admin.ModelAdmin):
    list_display = (
        'value',
        'mnosh',
        'price'
    )

class Metalkolvoryadlag(models.Model):
    value = models.CharField("Значение поля", max_length=300)
    mnosh = models.DecimalField("Умножить результат при выборе на", max_digits=100, decimal_places=5)
    price = models.DecimalField("Прибавлять за каждый каждый метр", max_digits=100, decimal_places=2)
    class Meta:
        verbose_name = 'Количество рядов'
        verbose_name_plural = '[Metal] Количество рядов'


class MetalmetodystanovkiAdmin(admin.ModelAdmin):
    list_display = (
        'value',
        'mnosh',
        'price'
    )

class Metalmetodystanovki(models.Model):
    value = models.CharField("Значение поля", max_length=300)
    mnosh = models.DecimalField("Умножить результат при выборе на", max_digits=100, decimal_places=5)
    price = models.DecimalField("Прибавлять за каждый каждый метр", max_digits=100, decimal_places=2)
    class Meta:
        verbose_name = 'Метод установки'
        verbose_name_plural = '[Metal] Метод установки'


class MetalrazmerAdmin(admin.ModelAdmin):
    list_display = (
        'value',
        'mnosh',
        'price'
    )

class Metalrazmer(models.Model):
    value = models.CharField("Значение поля", max_length=300)
    mnosh = models.DecimalField("Умножить результат при выборе на", max_digits=100, decimal_places=5)
    price = models.DecimalField("Прибавлять за каждый каждый метр", max_digits=100, decimal_places=2)
    class Meta:
        verbose_name = 'Размер и толщина столбцов'
        verbose_name_plural = '[Metal] Размер и толщина столбцов'


class MetalshagAdmin(admin.ModelAdmin):
    list_display = (
        'value',
        'mnosh',
        'price'
    )

class Metalshag(models.Model):
    value = models.CharField("Значение поля", max_length=300)
    mnosh = models.DecimalField("Умножить результат при выборе на", max_digits=100, decimal_places=5)
    price = models.DecimalField("Прибавлять за каждый каждый метр", max_digits=100, decimal_places=2)
    class Meta:
        verbose_name = 'Шаг между столбами'
        verbose_name_plural = '[Metal] Шаг между столбами'


class MetalpaintAdmin(admin.ModelAdmin):
    list_display = (
        'value',
        'mnosh',
        'price'
    )

class Metalpaint(models.Model):
    value = models.CharField("Значение поля", max_length=300)
    mnosh = models.DecimalField("Умножить результат при выборе на", max_digits=100, decimal_places=5)
    price = models.DecimalField("Прибавлять за каждый каждый метр", max_digits=100, decimal_places=2)
    class Meta:
        verbose_name = 'Покраска'
        verbose_name_plural = '[Metal] Покраска'


class MetalstandartAdmin(admin.ModelAdmin):
    list_display = (
        'value',
        'mnosh',
        'price'
    )

class Metalstandart(models.Model):
    value = models.CharField("Значение поля", max_length=300)
    mnosh = models.DecimalField("Умножить результат при выборе на", max_digits=100, decimal_places=5)
    price = models.DecimalField("Прибавлять за каждый каждый метр", max_digits=100, decimal_places=2)
    class Meta:
        verbose_name = 'Калитка Стандарт'
        verbose_name_plural = '[Metal] Калитка Стандарт'

class MetalraspashAdmin(admin.ModelAdmin):
    list_display = (
        'value',
        'mnosh',
        'price'
    )

class Metalraspash(models.Model):
    value = models.CharField("Значение поля", max_length=300)
    mnosh = models.DecimalField("Умножить результат при выборе на", max_digits=100, decimal_places=5)
    price = models.DecimalField("Прибавлять за каждый каждый метр", max_digits=100, decimal_places=2)
    class Meta:
        verbose_name = 'Распашные ворота'
        verbose_name_plural = '[Metal] Распашные ворота'


class MetalotkatAdmin(admin.ModelAdmin):
    list_display = (
        'value',
        'mnosh',
        'price'
    )

class Metalotkat(models.Model):
    value = models.CharField("Значение поля", max_length=300)
    mnosh = models.DecimalField("Умножить результат при выборе на", max_digits=100, decimal_places=5)
    price = models.DecimalField("Прибавлять за каждый каждый метр", max_digits=100, decimal_places=2)
    class Meta:
        verbose_name = 'Откатные (сдвижные) ворота'
        verbose_name_plural = '[Metal] Откатные (сдвижные) ворота'


class MetaldetektprotektAdmin(admin.ModelAdmin):
    list_display = (
        'value',
        'mnosh',
        'price'
    )

class Metaldetektprotekt(models.Model):
    value = models.CharField("Значение поля", max_length=300)
    mnosh = models.DecimalField("Умножить результат при выборе на", max_digits=100, decimal_places=5)
    price = models.DecimalField("Прибавлять за каждый каждый метр", max_digits=100, decimal_places=2)
    class Meta:
        verbose_name = 'Защитная декоративная планка'
        verbose_name_plural = '[Metal] Защитная декоративная планка'

class MetaldemontashAdmin(admin.ModelAdmin):
    list_display = (
        'value',
        'mnosh',
        'price'
    )

class Metaldemontash(models.Model):
    value = models.CharField("Значение поля", max_length=300)
    mnosh = models.DecimalField("Умножить результат при выборе на", max_digits=100, decimal_places=5)
    price = models.DecimalField("Прибавлять за каждый каждый метр", max_digits=100, decimal_places=2)
    class Meta:
        verbose_name = 'Демонтаж старого забора'
        verbose_name_plural = '[Metal] Демонтаж старого забора'


class MetalkmMkadAdmin(admin.ModelAdmin):
    list_display = (
        'value',
        'mnosh',
        'price'
    )


class MetalkmMkadAdmin(admin.ModelAdmin):
    list_display = (
        'start',
        'end',
        'price',
        'mnosh'
    )


class MetalkmMkad(models.Model):
    start = models.DecimalField("Начало промежутка", max_digits=100, decimal_places=0)
    end = models.DecimalField("Конец промежутка", max_digits=100, decimal_places=0)
    price = models.DecimalField("Прибавлять за каждый каждый метр", max_digits=100, decimal_places=2)
    mnosh = models.DecimalField("Умножить результат при выборе на", max_digits=100, decimal_places=5)

    class Meta:
        verbose_name = 'расстояние МКАД'
        verbose_name_plural = '[Metal] Количество км от МКАД'
