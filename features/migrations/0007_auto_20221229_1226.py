# Generated by Django 3.2 on 2022-12-29 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0006_brochures'),
    ]

    operations = [
        migrations.AddField(
            model_name='companysetup',
            name='mission',
            field=models.TextField(default='a'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='companysetup',
            name='vision',
            field=models.TextField(default='a'),
            preserve_default=False,
        ),
    ]
