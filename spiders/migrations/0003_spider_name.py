# Generated by Django 2.0.7 on 2018-07-31 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spiders', '0002_auto_20180731_2037'),
    ]

    operations = [
        migrations.AddField(
            model_name='spider',
            name='name',
            field=models.CharField(default='示例爬虫', max_length=20, verbose_name='爬虫'),
        ),
    ]
