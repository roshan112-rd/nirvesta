# Generated by Django 3.2 on 2022-12-30 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0017_auto_20221230_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shareholder',
            name='address',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='shareholder',
            name='contact',
            field=models.CharField(max_length=200),
        ),
    ]
