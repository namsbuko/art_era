# Generated by Django 2.0.3 on 2018-03-21 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0010_auto_20180321_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='about_yourself',
            field=models.TextField(blank=True, default='', max_length=5000),
        ),
    ]
