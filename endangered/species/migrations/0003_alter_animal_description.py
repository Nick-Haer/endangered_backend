# Generated by Django 3.2.7 on 2021-09-11 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('species', '0002_auto_20210911_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='description',
            field=models.CharField(default='none', max_length=10000),
        ),
    ]
