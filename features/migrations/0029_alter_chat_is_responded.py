# Generated by Django 3.2 on 2023-01-03 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0028_alter_chat_is_responded'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='is_responded',
            field=models.BooleanField(default=1),
        ),
    ]
