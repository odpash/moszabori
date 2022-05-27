from django.db import models
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
# import PIL

# Create your models here.
STATUS_CHOICES = (
    ('draft', 'Черновик'),
    ('published', 'Опубликовать'),
)
POST_TYPE_CHOICES = (
    ('image', 'Изображение'),
    ('video', 'Видео'),
)

PAGE_TEMPLATE_CHOICES = (
    ('about', 'home/about-us-template.html'),
    ('service', 'home/services-template.html'),
)

SERVICE_BGCOLOR = (
    ('0', 'Белый'),
    ('1', 'Основной'),
)

class SEO_Optimiser(models.Model):
    Title = models.CharField(_("Название"), max_length=60, blank=True, null=True,  default='', help_text="Enter the Title. Max: 60 characters")
    Content = models.TextField(_("Контент"), max_length=165, blank=True, null=True, default='',help_text="Enter the content. Max: 165 characters")
    Keywords = models.TextField('Ключевые слова', max_length=200, blank=True, null=True, default='', help_text='Enter keywords, max 200 symbols' )
    Image = ProcessedImageField(upload_to='SEO/%Y/%m/%d/',
                            processors=[ResizeToFill(1200, 627)],
                            format='JPEG',
                            options={'quality': 60}, blank=True)
    # Link = models.CharField("Link", max_length=100, blank=True, null=True, unique=True, help_text="Enter the link. Ex.: home-page or {% url 'home' %}")
    PageName = models.CharField("Имя страницы", max_length=55, blank=True, null=True,  default='', help_text="This field is just for a note for the admins. For which page you want to add the SEO?")
    seoid = models.IntegerField("SEO id", default=0, blank=True, unique=True, null=True, help_text="This text is used in sourceviews.py")

    def __str__(self):
        return str(self.seoid) + " " +self.PageName
    
    class Meta:
        verbose_name = 'SEO Поле'
        verbose_name_plural = 'SEO Поля'

@receiver(post_delete, sender=SEO_Optimiser)
def SEO_OptimiserImages_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.Image.delete(False)

class Page(models.Model):
    Title = models.CharField(_("Название"), blank=True, null=True, max_length=100, help_text="Enter the Title")
    # Slug = models.CharField(max_length=100, blank=True, null=True, unique=True, help_text="Enter the link. Ex.: eto-publikaciya")
    # ShortDesc = models.TextField("Короткое описание", max_length=165, null=True, blank=True, help_text="Enter the short description of the page using 165 symbols")
    Content = RichTextUploadingField("Контент", blank=True, null=True, help_text="Введите контент")
    Image = ProcessedImageField(upload_to='pages/%Y/%m/%d/',
                            processors=[ResizeToFill(1200, 768)],
                            format='JPEG',
                            options={'quality': 60}, blank=True)
    image_thumbnail = ImageSpecField(source='Image',
                                 processors=[ResizeToFill(768, 500)],
                                 format='JPEG',
                                #  options={'quality': 60}
                                 )
    template = models.CharField('Шаблон', max_length=20, blank=True, null=True, choices=PAGE_TEMPLATE_CHOICES, default='about', help_text='Select a template')                                 
    sortingIndex = models.IntegerField("Индекс сортировки",default=0, blank=True)
    SEO = models.ForeignKey(SEO_Optimiser, on_delete=models.CASCADE, null=True, blank=True)
    pageid = models.IntegerField("ID страницы", default=1, blank=True, help_text="This value is used in sourceviews.py")
    Created = models.DateTimeField(auto_now_add=True)  
    Updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='published')

    def __str__(self):
        return self.Title
    
    class Meta:
        ordering = (('-Created'),)
        # index_together = (('id', 'Slug'),)
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'

        
class FAQ(models.Model):
    Title = models.CharField("Вопрос", max_length=300, blank=True, null=True,  help_text="Enter the Title. Max: 200 characters")
    Content = RichTextUploadingField("Ответ", blank=True, null=True, default='',help_text="Enter the content.")
    sortingIndex = models.IntegerField("Индекс сортировки",default=0, blank=True)

    def __str__(self):
        return self.Title
    
    class Meta:
        verbose_name = 'Вопрос и ответ'
        verbose_name_plural = 'Вопросы и ответы'



class PricelistCategory(models.Model):
    Title = models.CharField("Категория услуги", max_length=300, blank=True, null=True,  help_text="Введите категорию услуги")

    def __str__(self):
        return self.Title

    class Meta:
        verbose_name = 'Категория Прайскурант'
        verbose_name_plural = 'Категории Прайскурантов'        

class Pricelist(models.Model):
    # sid = models.IntegerField("Индекс услуги", default=0, blank=True)
    Title = models.CharField("Наименование услуги", max_length=300, blank=True, null=True,  help_text="Наименование прайса")
    Measurement = models.CharField("Единица", max_length=50, blank=True, null=True,  help_text="Единица")
    Price = models.CharField("Стоимость", max_length=50, blank=True, null=True,  help_text="Единица")
    Category = models.ForeignKey(PricelistCategory, on_delete=models.SET_NULL, blank=True, null=True)
    sortingIndex = models.IntegerField("Индекс сортировки",default=0, blank=True)


    def __str__(self):
        return self.Title
    
    class Meta:
        verbose_name = 'Прайскурант'
        verbose_name_plural = 'Прайскуранты'  


class ServiceCategory(models.Model):
    Title = models.CharField("Название тип забора", max_length=100, blank=True, null=True,  help_text="Введите категорию услуги")
    Slug = models.CharField(max_length=100, blank=True, null=True, unique=True, help_text="Ссылка категория услуги")
    Content = RichTextUploadingField("Описание", blank=True, null=True, help_text="Короткое описание ")
    ShortDesc = models.TextField("Короткое описание", max_length=165, null=True, blank=True, help_text="Короткое описание сервиса")
    Image = ProcessedImageField(upload_to='zabory/categories/%Y-%m-%d/',
                            processors=[ResizeToFill(1200, 768)],
                            format='JPEG',
                            # options={'quality': 60}, 
                            blank=True, null=True)
    image_thumbnail = ImageSpecField(source='Image',
                                 processors=[ResizeToFill(390, 290)],
                                #  processors=[ResizeToFit(width=970, upscale=False)]
                                 format='JPEG',
                                #  options={'quality': 60}
                                 )

    def __str__(self):
        return self.Title


    class Meta:
        verbose_name = 'Тип забора'
        verbose_name_plural = 'Типы забора'  

    def get_absolute_url(self):
        return reverse('home:zaborCategory', args = [self.Slug]) 



@receiver(post_delete, sender=ServiceCategory)
def ServiceCategoryImages_deleter(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.Image.delete(False)
    

class Services(models.Model):
    # sid = models.IntegerField("Индекс услуги", default=0, blank=True)
    ShortTitle = models.CharField("Короткое имя сервиса", max_length=30, blank=True, null=True,  help_text="Наименование сервиса")
    Title = models.CharField("Длинное имя сервиса", max_length=65, blank=True, null=True,  help_text="Наименование сервиса")
    Slug = models.CharField(max_length=100, blank=True, null=True, unique=True, help_text="Ссылка сервиса")
    Category = models.ForeignKey(ServiceCategory, on_delete=models.SET_NULL, blank=True, null=True)
    ShortDesc = models.TextField("Короткое описание", max_length=165, null=True, blank=True, help_text="Короткое описание сервиса")
    Content = RichTextUploadingField("Контент", blank=True, null=True, help_text="Короткое описание сервиса")
    Image = ProcessedImageField(upload_to='services/%Y-%m-%d/',
                            # processors=[ResizeToFill(1200, 768)],
                            format='JPEG',
                            # options={'quality': 60}, 
                            blank=True)
    image_thumbnail = ImageSpecField(source='Image',
                                 processors=[ResizeToFill(390, 290)],
                                #  processors=[ResizeToFit(width=970, upscale=False)]
                                 format='JPEG',
                                #  options={'quality': 60}
                                 )
    # boxcolor = models.CharField("Цвет фона", max_length=30, choices=SERVICE_BGCOLOR, default='dreamit-service-box-inner')
    actualPrice = models.IntegerField("Обычная цена",default=0, blank=True, help_text="220000")
    discountedPrice = models.IntegerField("Цена со скидкой",default=0, blank=True, help_text="200000")
    
    sortingIndex = models.IntegerField("Индекс сортировки",default=0, blank=True)

    Created = models.DateTimeField(auto_now_add=True)  
    Updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='published')

    # SEO = models.ForeignKey(SEO_Optimiser, on_delete=models.CASCADE, null=True, blank=True)
    # Measurement = models.CharField("Единица", max_length=50, blank=True, null=True,  help_text="Единица")
    # Price = models.CharField("Стоимость", max_length=50, blank=True, null=True,  help_text="Единица")

# STATIC_ROOT = os.path.join(BASE_DIR, "static")ba
    def __str__(self):
        return self.Title
    
    class Meta:
        verbose_name = 'Забор'
        verbose_name_plural = 'Заборы'  
    
    def get_absolute_url(self):
        return reverse('home:zaborDetails', args = [self.Slug]) 

@receiver(post_delete, sender=Services)
def ServicesImages_deleter(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.Image.delete(False)

class NavesCategory(models.Model):
    Title = models.CharField("Тип Навеса", max_length=100, blank=True, null=True,  help_text="Введите категорию ")
    Slug = models.CharField(max_length=100, blank=True, null=True, unique=True, help_text="Ссылка категория ")
    Content = RichTextUploadingField("Описание", blank=True, null=True, help_text="Короткое описание ")
    ShortDesc = models.TextField("Короткое описание", max_length=165, null=True, blank=True, help_text="Короткое описание сервиса")
    Image = ProcessedImageField(upload_to='navesy/%Y-%m-%d/',
                            # processors=[ResizeToFill(1200, 768)],
                            format='JPEG',
                            # options={'quality': 60}, 
                            blank=True)
    image_thumbnail = ImageSpecField(source='Image',
                                 processors=[ResizeToFill(390, 290)],
                                #  processors=[ResizeToFit(width=970, upscale=False)]
                                 format='JPEG',
                                #  options={'quality': 60}
                                 )

    def __str__(self):
        return self.Title

    class Meta:
        verbose_name = 'Тип навеса'
        verbose_name_plural = 'Типы навесов'  
    
    def get_absolute_url(self):
        return reverse('home:navesCategory', args = [self.Slug]) 

@receiver(post_delete, sender=NavesCategory)
def NavesCategoryImages_deleter(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.Image.delete(False)

class Naves(models.Model):
    # sid = models.IntegerField("Индекс услуги", default=0, blank=True)
    ShortTitle = models.CharField("Короткое имя сервиса", max_length=30, blank=True, null=True,  help_text="Наименование сервиса")
    Title = models.CharField("Длинное имя сервиса", max_length=65, blank=True, null=True,  help_text="Наименование сервиса")
    Slug = models.CharField(max_length=100, blank=True, null=True, unique=True, help_text="Ссылка сервиса")
    Category = models.ForeignKey(NavesCategory, on_delete=models.SET_NULL, blank=True, null=True)
    ShortDesc = models.TextField("Короткое описание", max_length=165, null=True, blank=True, help_text="Короткое описание сервиса")
    Content = RichTextUploadingField("Контент", blank=True, null=True, help_text="Короткое описание сервиса")
    Image = ProcessedImageField(upload_to='navesy/%Y-%m-%d/',
                            # processors=[ResizeToFill(1200, 768)],
                            format='JPEG',
                            # options={'quality': 60}, 
                            blank=True)
    image_thumbnail = ImageSpecField(source='Image',
                                 processors=[ResizeToFill(390, 290)],
                                #  processors=[ResizeToFit(width=970, upscale=False)]
                                 format='JPEG',
                                #  options={'quality': 60}
                                 )
    # boxcolor = models.CharField("Цвет фона", max_length=30, choices=SERVICE_BGCOLOR, default='dreamit-service-box-inner')
    actualPrice = models.IntegerField("Обычная цена",default=0, blank=True, help_text="220000")
    discountedPrice = models.IntegerField("Цена со скидкой",default=0, blank=True, help_text="200000")
    sortingIndex = models.IntegerField("Индекс сортировки",default=0, blank=True)
    Created = models.DateTimeField(auto_now_add=True)  
    Updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='published')

    # SEO = models.ForeignKey(SEO_Optimiser, on_delete=models.CASCADE, null=True, blank=True)
    # Measurement = models.CharField("Единица", max_length=50, blank=True, null=True,  help_text="Единица")
    # Price = models.CharField("Стоимость", max_length=50, blank=True, null=True,  help_text="Единица")

# STATIC_ROOT = os.path.join(BASE_DIR, "static")ba
    def __str__(self):
        return self.Title
    
    class Meta:
        verbose_name = 'Навес'
        verbose_name_plural = 'Навесы'  
    
    def get_absolute_url(self):
        return reverse('home:navesDetails', args = [self.Slug]) 

@receiver(post_delete, sender=Naves)
def NavesImages_deleter(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.Image.delete(False)



class PortfolioCategory(models.Model):
    Title = models.CharField("Категория портфолио", max_length=100, blank=True, null=True,  help_text="Введите категорию портфолио")
    Slug = models.CharField(max_length=100, blank=True, null=True, unique=True, help_text="Ссылка категория портфолио")

    def __str__(self):
        return self.Title

    class Meta:
        verbose_name = 'Категория портфолио'
        verbose_name_plural = 'Категории портфолио'  

class Portfolio(models.Model):
    # sid = models.IntegerField("Индекс услуги", default=0, blank=True)
    ShortTitle = models.CharField("Короткое имя портфолио", max_length=30, blank=True, null=True,  help_text="Наименование портфолио")
    Title = models.CharField("Длинное имя портфолио", max_length=65, blank=True, null=True,  help_text="Наименование портфолио")
    Slug = models.CharField(max_length=100, blank=True, null=True, unique=True, help_text="Ссылка портфолио")
    Category = models.ForeignKey(PortfolioCategory, on_delete=models.SET_NULL, blank=True, null=True)
    ShortDesc = models.TextField("Короткое описание", max_length=165, null=True, blank=True, help_text="Короткое описание портфолио")
    Content = RichTextUploadingField("Польное описание", blank=True, null=True, help_text="Короткое описание портфолио")
    Image = ProcessedImageField(upload_to='portfolio/%Y-%m-%d/',
                            processors=[ResizeToFill(1200, 768)],
                            format='JPEG',
                            options={'quality': 60}, blank=True)
    image_thumbnail = ImageSpecField(source='Image',
                                 processors=[ResizeToFill(768, 500)],
                                 format='JPEG',
                                #  options={'quality': 60}
                                 )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='published')
    sortingIndex = models.IntegerField("Индекс сортировки",default=0, blank=True)
    clientName = models.CharField("Имя клиента", max_length=50, blank=True, null=True,  help_text="Имя и фамилия клиента")
    Created = models.DateTimeField("Дата окончания", auto_now_add=True)  
    Updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.Title
    
    class Meta:
        verbose_name = 'Фото работы'
        verbose_name_plural = 'Фото работы'  
    
    def get_absolute_url(self):
        return reverse('home:portfolioDetails', args = [self.Slug]) 

@receiver(post_delete, sender=Portfolio)
def PortfolioImages_deleter(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.Image.delete(False)