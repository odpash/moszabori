from django.db import models
from django.contrib import admin
from django.urls import reverse
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models.signals import post_delete
from django.dispatch.dispatcher import receiver
from django.contrib.auth.models import User 
from django.conf import settings
from imagekit.processors import ResizeToFill  
from imagekit.models import ImageSpecField, ProcessedImageField   
from django.utils.translation import gettext_lazy  as _  
from django.utils import timezone

STATUS_CHOICES = (
    ('draft', 'Черновик'),
    ('published', 'Опубликовать'),
)
POST_TYPE_CHOICES = (
    ('image', 'Изображение'),
    ('video', 'Видео'),
)


class StolbaAdmin(admin.ModelAdmin):
    list_display = (
        'tipStolba',
        'sechenieStolba',
        'tolshinaStolba',
        'cena',
        'kolichestvo',
        'edinicaIzmereniya',
        )
    # list_filter =  ['PageName', 'Title', ]
    save_as = True
    # readonly_fields = ("PageName", 'id')
    list_editable = ['cena', ]


class PokritieAdmin(admin.ModelAdmin):
    list_display = (
        'Title',
        'cena',
        'marka',
        'kolVolna',
        'tolshina',
        'kraska',
        'kolichestvo',
        'edIzmer',
    )
    list_filter = [
        'marka',
        'Title',
        'kraska',

    ]
    save_as = True
    list_editable = (
        'marka',
        'kolVolna',
        'cena',

    )


class KraskaAdmin(admin.ModelAdmin):
    list_display = (
        'Title',
        'kolichestvo',
        'edIzmer',
        'cena',
    )
    # list_filter =  [
    #                 'marka',
    #                 'Title',
    #                 'kraska',

    #                 ]
    save_as = True
    # readonly_fields = ("PageName", 'id')


class ServicesAndMaterialsAdmin(admin.ModelAdmin):
    list_display = (
                'Title',

                'cena',
                'Slug',
                'param1',
                'param2',
                'param3',
                'kolichestvo',
                'edIzmer',
                'smtip',

            )
    list_filter =  [
                    'smtip',
                    ]
    save_as = True
    # readonly_fields = ("smtip",)
    list_editable = ['cena', ]


class LaborCostAdmin(admin.ModelAdmin):
    list_display = (
        'Title',
        'cena',
        'workType',
        'Slug',
        'param1',
        'param2',
        'param3',
        'kolichestvo',
        'edIzmer',
    )
    list_filter = [
        'workType',

    ]
    save_as = True
    # readonly_fields = ("smtip",)
    list_editable = ['cena', ]


class ProfnastilTipStolba(models.Model):
    Title = models.CharField("Тип/Наименование столбы", max_length=100, blank=True, null=True,  help_text="Введите тип столбы")
    # Slug = models.CharField(max_length=100, blank=True, null=True, unique=True, help_text="Ссылка категория портфолио")

    def __str__(self):
        return self.Title

    class Meta:
        verbose_name = 'Тип столб'
        verbose_name_plural = '[Profnastil] Тип столба'

class ProfnastilSechenieStolba(models.Model):
    Title = models.CharField("Сечение столбы", max_length=100, blank=True, null=True,  help_text="Введите сечение столбы")
    edIzmereniya = models.CharField("Единица измерения", max_length=100, blank=True, null=True,  help_text="Введите единицу измерения")

    # Slug = models.CharField(max_length=100, blank=True, null=True, unique=True, help_text="Ссылка категория портфолио")

    def __str__(self):
        return self.Title

    class Meta:
        verbose_name = 'Сечение столб'
        verbose_name_plural = '[Profnastil] Сечение столбы'

class ProfnastilTolshinaStolba(models.Model):
    Title = models.CharField("Толшина столбы", max_length=100, blank=True, null=True,  help_text="Введите толшина столбы")
    edIzmereniya = models.CharField("Единица измерения", max_length=100, blank=True, null=True,  help_text="Введите единицу измерения толшина столбы")

    # Slug = models.CharField(max_length=100, blank=True, null=True, unique=True, help_text="Ссылка категория портфолио")

    def __str__(self):
        return self.Title + self.edIzmereniya

    class Meta:
        verbose_name = 'Толшина столб'
        verbose_name_plural = '[Profnastil] Толшина столбы'

class ProfnastilEdinicaIzmereniya(models.Model):
    Title = models.CharField("Единица измерения", max_length=100, blank=True, null=True,  help_text="Введите единица измерения")
    # Title = models.CharField("Единица измерения", max_length=100, blank=True, null=True,  help_text="Введите единица измерения")

    # Slug = models.CharField(max_length=100, blank=True, null=True, unique=True, help_text="Ссылка категория портфолио")

    def __str__(self):
        return self.Title

    class Meta:
        verbose_name = 'Единица измерения'
        verbose_name_plural = '[Profnastil] Единица измерении'

class ProfnastilStolba(models.Model):
    # Title = models.CharField("Cтолба", max_length=100, blank=True, null=True,  help_text="Введите толшина столбы")
    # Slug = models.CharField(max_length=100, blank=True, null=True, unique=True, help_text="Ссылка категория портфолио")
    tipStolba = models.ForeignKey(ProfnastilTipStolba, on_delete=models.SET_NULL, blank=True, null=True)
    sechenieStolba = models.ForeignKey(ProfnastilSechenieStolba, on_delete=models.SET_NULL, blank=True, null=True)
    tolshinaStolba = models.ForeignKey(ProfnastilTolshinaStolba, on_delete=models.SET_NULL, blank=True, null=True)
    edinicaIzmereniya = models.ForeignKey(ProfnastilEdinicaIzmereniya, on_delete=models.SET_NULL, blank=True, null=True)
    kolichestvo = models.IntegerField("Количество", default=0, blank=True, null=True, help_text="Количество")
    cena = models.IntegerField("Цена единицы", default=0, blank=True, null=True, help_text="Цена")

    def __str__(self):
        return str(self.tipStolba.Title)

    class Meta:
        verbose_name = 'Столба'
        verbose_name_plural = '[Profnastil] Столбы'


class ProfnastilPokritie(models.Model):
    MARKA = (('1', 'C'),) 
    EDIZMERENIYA = (('1', 'м2'),)
    KOLVOLNA = ( ('1', '8'),  ('2', '20'), ('3', '21'),)

    TOLSHINA = (
        ('1', '0.30'),   ('2', '0.35'),
        ('3', '0.40'),   ('4', '0.45'),  ('5', '0.50'),)

    KRASKA = (('1', 'односторонный'),
            ('2', 'двусторонный'), ('3', 'оцинкованный'), )
    
    Title = models.CharField("Название покрытия", max_length=100, blank=True, null=True,  help_text="Введите названия покрытия")
    marka = models.CharField('Марка', max_length=20, blank=True, null=True, choices=MARKA, default='1', help_text='Выберите толшину покрытия')                                 
    kolVolna = models.CharField('Кол. волны', max_length=20, blank=True, null=True, choices=KOLVOLNA, default='1', help_text='Выберите количество волн')                                 
    tolshina = models.CharField('Толшина', max_length=20, blank=True, null=True, choices=TOLSHINA, default='1', help_text='Выберите толшину покрытия')                                 
    kraska = models.CharField('Краска', max_length=20, blank=True, null=True, choices=KRASKA, default='1', help_text='Выберите толшину покрытия')                                 
    
    kolichestvo = models.IntegerField("Количество", default=1, blank=True, null=True, help_text="Количество")
    edIzmer = models.CharField('Единица Измерения', max_length=20, blank=True, null=True, choices=EDIZMERENIYA, default='1', help_text='Выберите толшину покрытия')                                 
    # edinicaIzmereniya = models.ForeignKey(EdinicaIzmereniya, on_delete=models.SET_NULL, blank=True, null=True)
    cena = models.IntegerField("Цена единицы", default=0, blank=True, null=True, help_text="Цена")

    def __str__(self):
        return str(self.Title)

    class Meta:
        verbose_name = 'Тип покрытие'
        verbose_name_plural = '[Profnastil] Тип покрытия'


class ProfnastilKraska(models.Model):
    MARKA = (('1', 'C'),) 
    EDIZMERENIYA = (('1', 'пм'),)
    KRASKA = (('1', 'односторонный'),
            ('2', 'двусторонный'), ('3', 'оцинкованный'), )
    
    Title = models.CharField("Название покрытия", max_length=100, blank=True, null=True,  help_text="Введите названия покрытия")
    # marka = models.CharField('Марка', max_length=20, blank=True, null=True, choices=MARKA, default='1', help_text='Выберите толшину покрытия')                                 
    # kolVolna = models.CharField('Кол. волны', max_length=20, blank=True, null=True, choices=KOLVOLNA, default='1', help_text='Выберите количество волн')                                 
    # tolshina = models.CharField('Толшина', max_length=20, blank=True, null=True, choices=TOLSHINA, default='1', help_text='Выберите толшину покрытия')                                 
    # kraska = models.CharField('Краска', max_length=20, blank=True, null=True, choices=KRASKA, default='1', help_text='Выберите толшину покрытия')                                 
    
    kolichestvo = models.DecimalField("Количество", default=1.0, decimal_places=2, max_digits=10, blank=True, null=True, help_text="Количество")
    edIzmer = models.CharField('Единица Измерения', max_length=20, blank=True, null=True, choices=EDIZMERENIYA, default='1', help_text='Выберите толшину покрытия')                                 
    # edinicaIzmereniya = models.ForeignKey(EdinicaIzmereniya, on_delete=models.SET_NULL, blank=True, null=True)
    cena = models.DecimalField("Цена единицы", default=400.0, decimal_places=2, max_digits=10, blank=True, null=True, help_text="Цена")

    def __str__(self):
        return str(self.Title)

    class Meta:
        verbose_name = 'Краска'
        verbose_name_plural = '[Profnastil] Краски'


class ProfnastilServicesAndMaterials(models.Model):
    # MARKA = (('1', 'C'),) 
    EDIZMERENIYA = (('1', 'пм'), 
                    ('2', 'упак'), 
                    ('3', 'компл'),
                    ('4', 'шт'),
                    )
    SMTIP = (
                ('beton', 'Бетонирование'), 
                ('utrambovka', 'Утрамбовка'), 
                ('gruntovka', 'Грунтовка'),
                ('lagi', 'Лаги'),
                ('zaglushka', 'Заглушка'),
                ('zamosrezi', 'Саморезы'),
                ('planka', 'Планка'),
                ('kalitka', 'Калитка'),
                ('vorota', 'Ворота'),
                ('rabota', 'Работа'),
                ('drugoe', 'Другое'),
            )
    # KRASKA = (('1', 'односторонный'),
    #         ('2', 'двусторонный'), ('3', 'оцинкованный'), )
    smtip = models.CharField('Тип услуги/материала', max_length=20, blank=True, null=True, choices=SMTIP, default='drugoe', help_text='Выберите тип')                                 
    Title = models.CharField("Название усгули или материала", max_length=100, blank=True, null=True,  help_text="Введите названия усгули или материала")

    kolichestvo = models.DecimalField("Количество", default=1.0, decimal_places=2, max_digits=10, blank=True, null=True, help_text="Количество")
    edIzmer = models.CharField('Единица Измерения', max_length=20, blank=True, null=True, choices=EDIZMERENIYA, default='1', help_text='Выберите единицу')                                 
    param1 = models.CharField("Параметр 1", max_length=10, blank=True, null=True,  help_text="Например, высоту: 1.5")
    param2 = models.CharField("Параметр 2", max_length=10, blank=True, null=True,  help_text="Например, ширину: 2.5")
    param3 = models.CharField("Параметр 3", max_length=10, blank=True, null=True,  help_text="Например, толшину: 0.30")
    
    cena = models.DecimalField("Цена единицы", default=400.0, decimal_places=2, max_digits=10, blank=True, null=True, help_text="Цена")
    Slug = models.CharField("Ссылка", max_length=20, blank=True, null=True, unique=True,  help_text="Введите ссылку. Нельзя изменить! ")

    def __str__(self):
        return str(self.Title)

    class Meta:
        verbose_name = 'Другой  материал'
        verbose_name_plural = '[Profnastil] Другие материалы'


class ProfnastilLaborCost(models.Model):
    # MARKA = (('1', 'C'),) 
    EDIZMERENIYA = (('1', 'пм'), 
                    ('2', 'упак'), 
                    ('3', 'компл'),
                    ('4', 'шт'),
                    )

    WORKTYPE = (
                ('ustZaborProfnast', 'Установка забора из профнастиля'), 
                ('drugoe', 'Другое'),
            )
    # KRASKA = (('1', 'односторонный'),
    #         ('2', 'двусторонный'), ('3', 'оцинкованный'), )
    workType = models.CharField('Тип работы', max_length=20, blank=True, null=True, choices=WORKTYPE, default='drugoe', help_text='Выберите тип')                                 
    Title = models.CharField("Название работы", max_length=100, blank=True, null=True,  help_text="Введите названия работы")
    kolichestvo = models.DecimalField("Количество", default=1.0, decimal_places=2, max_digits=10, blank=True, null=True, help_text="Количество")
    edIzmer = models.CharField('Единица Измерения', max_length=20, blank=True, null=True, choices=EDIZMERENIYA, default='1', help_text='Выберите единицу')                                 
    param1 = models.CharField("Параметр 1", max_length=10, blank=True, null=True,  help_text="Например, высоту: 1.5")
    param2 = models.CharField("Параметр 2", max_length=10, blank=True, null=True,  help_text="Например, ширину: 2.5")
    param3 = models.CharField("Параметр 3", max_length=10, blank=True, null=True,  help_text="Например, толшину: 0.30")
    cena = models.DecimalField("Цена единицы", default=400.0, decimal_places=2, max_digits=10, blank=True, null=True, help_text="Цена")
    Slug = models.CharField("Ссылка", max_length=20, blank=True, null=True,  help_text="Введите ссылку. Нельзя изменить! ")

    def __str__(self):
        return str(self.Title)

    class Meta:
        verbose_name = 'Стоимость работы'
        verbose_name_plural = '[Profnastil] Стоимость работы'
