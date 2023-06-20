# Generated by Django 4.2.1 on 2023-06-03 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_product_category_delete_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Имя')),
                ('number', models.IntegerField(max_length=11, verbose_name='Номер телефона')),
                ('email', models.EmailField(max_length=40, verbose_name='Почта')),
                ('message', models.CharField(max_length=300, verbose_name='Сообщение')),
            ],
        ),
        migrations.AlterField(
            model_name='worker',
            name='post',
            field=models.CharField(max_length=80, verbose_name='Должность'),
        ),
    ]