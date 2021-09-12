# Generated by Django 3.2.7 on 2021-09-11 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('latin_name', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('image_url', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
    ]
