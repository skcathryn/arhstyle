# Generated by Django 4.2.1 on 2023-06-02 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_worker'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
