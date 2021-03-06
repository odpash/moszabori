# Generated by Django 3.2.9 on 2022-02-25 06:04

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20211116_2207'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='faq',
            options={'verbose_name': 'Вопрос и ответ', 'verbose_name_plural': 'Вопросы и ответы'},
        ),
        migrations.AlterModelOptions(
            name='page',
            options={'ordering': ('-Created',), 'verbose_name': 'Страница', 'verbose_name_plural': 'Страницы'},
        ),
        migrations.AlterModelOptions(
            name='seo_optimiser',
            options={'verbose_name': 'SEO Поле', 'verbose_name_plural': 'SEO Поля'},
        ),
        migrations.AlterField(
            model_name='faq',
            name='Content',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default='', help_text='Enter the content.', null=True, verbose_name='Ответ'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='Title',
            field=models.CharField(blank=True, help_text='Enter the Title. Max: 200 characters', max_length=300, null=True, verbose_name='Вопрос'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='sortingIndex',
            field=models.IntegerField(blank=True, default=0, verbose_name='Индекс сортировки'),
        ),
        migrations.AlterField(
            model_name='page',
            name='Content',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, help_text='Введите контент', null=True, verbose_name='Контент'),
        ),
        migrations.AlterField(
            model_name='page',
            name='Title',
            field=models.CharField(blank=True, help_text='Enter the Title', max_length=100, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='page',
            name='pageid',
            field=models.IntegerField(blank=True, default=1, help_text='This value is used in sourceviews.py', verbose_name='ID страницы'),
        ),
        migrations.AlterField(
            model_name='page',
            name='sortingIndex',
            field=models.IntegerField(blank=True, default=0, verbose_name='Индекс сортировки'),
        ),
        migrations.AlterField(
            model_name='page',
            name='status',
            field=models.CharField(choices=[('draft', 'Черновик'), ('published', 'Опубликовать')], default='published', max_length=10),
        ),
        migrations.AlterField(
            model_name='page',
            name='template',
            field=models.CharField(blank=True, choices=[('about', 'home/about-us-template.html'), ('service', 'home/services-template.html')], default='about', help_text='Select a template', max_length=20, null=True, verbose_name='Шаблон'),
        ),
        migrations.AlterField(
            model_name='seo_optimiser',
            name='Content',
            field=models.TextField(blank=True, default='', help_text='Enter the content. Max: 165 characters', max_length=165, null=True, verbose_name='Контент'),
        ),
        migrations.AlterField(
            model_name='seo_optimiser',
            name='Keywords',
            field=models.TextField(blank=True, default='', help_text='Enter keywords, max 200 symbols', max_length=200, null=True, verbose_name='Ключевые слова'),
        ),
        migrations.AlterField(
            model_name='seo_optimiser',
            name='PageName',
            field=models.CharField(blank=True, default='', help_text='This field is just for a note for the admins. For which page you want to add the SEO?', max_length=55, null=True, verbose_name='Имя страницы'),
        ),
        migrations.AlterField(
            model_name='seo_optimiser',
            name='Title',
            field=models.CharField(blank=True, default='', help_text='Enter the Title. Max: 60 characters', max_length=60, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='seo_optimiser',
            name='seoid',
            field=models.IntegerField(blank=True, default=0, help_text='This text is used in sourceviews.py', null=True, unique=True, verbose_name='SEO id'),
        ),
    ]
