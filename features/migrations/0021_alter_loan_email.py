# Generated by Django 3.2 on 2023-01-02 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0020_alter_companyprofile_investment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
