# Generated by Django 3.0.4 on 2020-06-15 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20200614_2227'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='image/'),
        ),
    ]
