from django.db import models

# Create your models here.


# 存储不同的爬虫
class Spider(models.Model):
    objects = models.Manager()
    name = models.CharField('爬虫', max_length=255, default='爬虫')

    class Meta:
        verbose_name = '爬虫'

    def __str__(self):
        return self.name


# 存储爬取的结果
class Result(models.Model):
    objects = models.Manager()
    url = models.TextField('网址', max_length=65536,
                           default='http://news.baidu.com/')
    reasults = models.TextField('结果', default=' ')
    name = models.ForeignKey(
        Spider, on_delete=models.SET_DEFAULT, default=1)

    class Meta:
        verbose_name = '结果'
        #verbose_name_pliral = '标签'
        ordering = ['id']

    def __str__(self):
        return self.name
