# Generated by Django 2.0.7 on 2018-07-31 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Spider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='爬虫', max_length=40, verbose_name='爬虫')),
                ('url', models.TextField(default='匿名', max_length=65536, verbose_name='网址')),
            ],
            options={
                'verbose_name': '小伙伴',
                'ordering': ['name'],
            },
        ),
    ]
