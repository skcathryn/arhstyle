# Generated by Django 4.2.1 on 2023-06-08 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_portfolio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='image_2',
            field=models.ImageField(blank=True, upload_to='static/main/img', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='image_3',
            field=models.ImageField(blank=True, upload_to='static/main/img', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='image_4',
            field=models.ImageField(blank=True, upload_to='static/main/img', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='image_5',
            field=models.ImageField(blank=True, upload_to='static/main/img', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='image_6',
            field=models.ImageField(blank=True, upload_to='static/main/img', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='image_7',
            field=models.ImageField(blank=True, upload_to='static/main/img', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='image_8',
            field=models.ImageField(blank=True, upload_to='static/main/img', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='image_9',
            field=models.ImageField(blank=True, upload_to='static/main/img', verbose_name='Изображение'),
        ),
    ]