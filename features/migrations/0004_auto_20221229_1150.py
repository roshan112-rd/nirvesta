# Generated by Django 3.2 on 2022-12-29 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0003_alter_slider_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='featured_image',
            field=models.ImageField(blank=True, null=True, upload_to='services'),
        ),
        migrations.AlterField(
            model_name='service',
            name='icon',
            field=models.ImageField(upload_to='services'),
        ),
    ]
