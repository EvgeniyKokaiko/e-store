# Generated by Django 3.2.5 on 2021-07-11 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20210711_1907'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='image',
        ),
        migrations.AddField(
            model_name='category',
            name='iconClassList',
            field=models.CharField(max_length=254, null=True, verbose_name='Icons'),
        ),
    ]
