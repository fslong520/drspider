#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 豆瓣爬虫 '

__author__ = 'fslong'

import ast  # 用于将字符串转为字典
import json
import multiprocessing
import os
import random
import re
import sys
import threading
import time
import traceback

import pyquery
import requests

from spider import Spider
# 用于存储照片的
from PIL import Image

from io import BytesIO



class Bilibili(Spider):
    def getTitlePic(self, url):
        self.url = url
        req = requests.get(self.url, headers=self.headers)
        PQreq=pyquery.PyQuery(req.text)
        for i in PQreq('meta').items():
            if i.attr.itemprop=='image':
                print('封面图片地址是：%s'%i.attr.content)
                self.downLoadPic(i.attr.content,url.split('/')[-1])
                return i.attr.content
        #<meta content="http://i2.hdslb.com/bfs/archive/8c5e02a3308d1bba0617db1049a530a83ecbe5d9.jpg" itemprop="image" data-vue-meta="true">
    def downLoadPic(self,url,picName):
        req = requests.get(url, headers=self.headers)
        image = Image.open(BytesIO(req.content))
        image.show()
        image.save(os.path.join(os.path.dirname(__file__),'img/'+picName+'.'+url.split('.')[-1]))
        print('图片保存完毕，请前往img目录下查看。')


if __name__ == '__main__':
    bilibili = Bilibili()
    picUrl=bilibili.getTitlePic(
        'https://www.bilibili.com/video/' + input('请输入要下载封面的视频代号：'), )
