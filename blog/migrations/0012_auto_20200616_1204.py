# Generated by Django 3.0.4 on 2020-06-16 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20200616_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='height_field',
            field=models.IntegerField(default=50),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='width_field',
            field=models.IntegerField(default=50),
        ),
    ]
