#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 多线程异步下载nyaso每日的图片 '

__author__ = 'fslong'

import asyncio
import multiprocessing
import random
import threading
import time
import traceback
import json

import pyquery
import requests
import urllib


class Nyaso(object):
    def __init__(self, *args, **kwargs):
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.18204'}
        req = requests.get('https://pic.nyaso.com/', headers=self.header)
        s = str(req.cookies['check']).split('%2C')[1]
        # 使用urllib库中的unquote函数对s进行转换，url当中不能有特殊符号和中文所以，一般都进行了encode处理，如果想要进行encode处理的画可以使用：urllib.parse.quote(s)
        s = urllib.parse.unquote(s, encoding='utf-8')
        print(s)
        self.urls = {'wallpaper': 'https://pic.nyaso.com/api/wallpaper.json',
                     'pixiv': 'https://pic.nyaso.com/api/pixiv.json'}
        self.params = {
            'wallpaper': {
                't': 'new',
                'p': 1,
                's': s,
            },
            'pixiv': {
                't': 'daily',
                'p': 1,
                's': s,
            }
        }
        self.cookies = {'Cookie': 'check=%s' % str(req.cookies['check'])}
        print(self.cookies)

    async def getnysasoPixivPic(self, page):
        params = self.params['pixiv']
        params['p'] = page
        req = requests.get(
            self.urls['pixiv'], params=params, headers=self.header)
        # print(req.text)
        dataJson = json.loads(req.text)
        for i in dataJson['lists']:
            print(i['title'])


if __name__ == '__main__':
    nyaso = Nyaso()
    loop = asyncio.get_event_loop()
    tasks = [nyaso.getnysasoPixivPic(i+1) for i in [5]]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
