# Generated by Django 3.2.9 on 2022-06-06 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0004_auto_20220606_2343'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='metalshtaketnik',
            name='visota',
        ),
    ]