# Generated by Django 4.2.1 on 2023-06-06 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_delete_reviews'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Имя')),
                ('comment', models.CharField(max_length=3000, verbose_name='Коментарий')),
            ],
        ),
    ]
