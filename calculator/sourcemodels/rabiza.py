from django.db import models
from django.contrib import admin


class RabizadlinazaboraAdmin(admin.ModelAdmin):
    list_display = (
        'start',
        'end',
        'price',
        'mnosh'
    )


class Rabizadlinazabora(models.Model):
    start = models.DecimalField("Начало промежутка", max_digits=100, decimal_places=0)
    end = models.DecimalField("Конец промежутка", max_digits=100, decimal_places=0)
    price = models.DecimalField("Прибавлять за каждый каждый метр", max_digits=100, decimal_places=2)
    mnosh = models.DecimalField("Умножить результат при выборе на", max_digits=100, decimal_places=5)

    class Meta:
        verbose_name = 'длину забора'
        verbose_name_plural = '[Rabiza] Длина забора'


class RabizavisotazaboraAdmin(admin.ModelAdmin):
    list_display = (
        'value',
        'mnosh',
        'price'
    )

class Rabizavisotazabora(models.Model):
    value = models.CharField("Значение поля", max_length=300)
    mnosh = models.DecimalField("Умножить результат при выборе на", max_digits=100, decimal_places=5)
    price = models.DecimalField("Прибавлять за каждый каждый метр", max_digits=100, decimal_places=2)
    class Meta:
        verbose_name = 'высоту забора'
        verbose_name_plural = '[Rabiza] Высота забора'



class RabizamethodystanovkistolbovAdmin(admin.ModelAdmin):
    list_display = (
        'value',
        'mnosh',
        'price'
    )


class Rabizamethodystanovkistolbov(models.Model):
    value = models.CharField("Значение поля", max_length=300)
    mnosh = models.DecimalField("Умножить результат при выборе на", max_digits=100, decimal_places=5)
    price = models.DecimalField("Прибавлять за каждый каждый метр", max_digits=100, decimal_places=2)
    class Meta:
        verbose_name = 'метод установки столбов'
        verbose_name_plural = '[Rabiza] Метод установки столбов'


class RabizarazmertolshinastolbAdmin(admin.ModelAdmin):
    list_display = (
        'value',
        'mnosh',
        'price'
    )



class Rabizarazmertolshinastolb(models.Model):
    value = models.CharField("Значение поля", max_length=300)
    mnosh = models.DecimalField("Умножить результат при выборе на", max_digits=100, decimal_places=5)
    price = models.DecimalField("Прибавлять за каждый каждый метр", max_digits=100, decimal_places=2)
    class Meta:
        verbose_name = 'размер и толщину столбов'
        verbose_name_plural = '[Rabiza] Размер и толщина столбов'


class RabizapokraskastolbAdmin(admin.ModelAdmin):
    list_display = (
        'value',
        'mnosh',
        'price'
    )




class Rabizapokraskastolb(models.Model):
    value = models.CharField("Значение поля", max_length=300)
    mnosh = models.DecimalField("Умножить результат при выборе на", max_digits=100, decimal_places=5)
    price = models.DecimalField("Прибавлять за каждый каждый метр", max_digits=100, decimal_places=2)
    class Meta:
        verbose_name = 'покраску столбов и секций'
        verbose_name_plural = '[Rabiza] Покраска столбов и секций'


class RabizaraspashnievorotaAdmin(admin.ModelAdmin):
    list_display = (
        'value',
        'mnosh',
        'price'
    )


class Rabizaraspashnievorota(models.Model):
    value = models.CharField("Значение поля", max_length=300)
    mnosh = models.DecimalField("Умножить результат при выборе на", max_digits=100, decimal_places=5)
    price = models.DecimalField("Прибавлять за каждый каждый метр", max_digits=100, decimal_places=2)
    class Meta:
        verbose_name = 'распашные ворота:'
        verbose_name_plural = '[Rabiza] Распашные ворота:'



class RabizakalitkastandartAdmin(admin.ModelAdmin):
    list_display = (
        'value',
        'mnosh',
        'price'
    )




class Rabizakalitkastandart(models.Model):
    value = models.CharField("Значение поля", max_length=300)
    mnosh = models.DecimalField("Умножить результат при выборе на", max_digits=100, decimal_places=5)
    price = models.DecimalField("Прибавлять за каждый каждый метр", max_digits=100, decimal_places=2)
    class Meta:
        verbose_name = 'Калитка "Стандарт"'
        verbose_name_plural = '[Rabiza] Калитка "Стандарт"'


class RabizashirinavorotAdmin(admin.ModelAdmin):
    list_display = (
        'value',
        'mnosh',
        'price'
    )



class Rabizashirinavorot(models.Model):
    value = models.CharField("Значение поля", max_length=300)
    mnosh = models.DecimalField("Умножить результат при выборе на", max_digits=100, decimal_places=5)
    price = models.DecimalField("Прибавлять за каждый каждый метр", max_digits=100, decimal_places=2)
    class Meta:
        verbose_name = 'ширину ворот'
        verbose_name_plural = '[Rabiza] Ширина ворот'


class RabizademontashvorotAdmin(admin.ModelAdmin):
    list_display = (
        'value',
        'mnosh',
        'price'
    )


class Rabizademontashvorot(models.Model):
    value = models.CharField("Значение поля", max_length=300)
    mnosh = models.DecimalField("Умножить результат при выборе на", max_digits=100, decimal_places=5)
    price = models.DecimalField("Прибавлять за каждый каждый метр", max_digits=100, decimal_places=2)
    class Meta:
        verbose_name = 'демонтаж старого забора:'
        verbose_name_plural = '[Rabiza] Демонтаж старого забора:'


class RabizakmmkadAdmin(admin.ModelAdmin):
    list_display = (
        'start',
        'end',
        'price',
        'mnosh'
    )


class Rabizakmmkad(models.Model):
    start = models.DecimalField("Начало промежутка", max_digits=100, decimal_places=0)
    end = models.DecimalField("Конец промежутка", max_digits=100, decimal_places=0)
    price = models.DecimalField("Прибавлять за каждый каждый метр", max_digits=100, decimal_places=2)
    mnosh = models.DecimalField("Умножить результат при выборе на", max_digits=100, decimal_places=5)

    class Meta:
        verbose_name = 'расстояние МКАД'
        verbose_name_plural = '[Rabiza] Количество км от МКАД'
