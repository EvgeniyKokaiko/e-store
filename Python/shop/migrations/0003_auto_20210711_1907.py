# Generated by Django 3.2.5 on 2021-07-11 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20210711_0051'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['-price'], 'verbose_name_plural': 'Items'},
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.FloatField(verbose_name='Price'),
        ),
    ]
