# Generated by Django 2.1 on 2018-08-20 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180820_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='addr',
            field=models.TextField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='author',
            name='qq',
            field=models.CharField(blank=True, default=None, max_length=10),
        ),
    ]
