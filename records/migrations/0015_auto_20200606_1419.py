# Generated by Django 3.0.4 on 2020-06-06 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0014_auto_20200606_1329'),
    ]

    operations = [
        migrations.RenameField(
            model_name='faculty',
            old_name='faculty',
            new_name='fac',
        ),
        migrations.RenameField(
            model_name='levels',
            old_name='level',
            new_name='lev',
        ),
        migrations.RenameField(
            model_name='schools',
            old_name='school',
            new_name='sch',
        ),
    ]
