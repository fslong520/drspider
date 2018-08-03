
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 爬虫 '

__author__ = 'fslong'


import ast  # 用于将字符串转为字典
import json
import multiprocessing
import os
import re
import threading
import time
import traceback

import pyquery
import requests
import random
import asyncio


class Spider(object):
    def __init__(self):
        self.path = os.path.dirname(__file__)
        self.startUrl = 'www.baidu.com'
        self.userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.18204'
        self.headers = {'User-Agent': self.userAgent, }
        self.num = 0
        self.results = []
        self.cookies = {'Cookie': ''}


if __name__ == "__main__":
    async def yiBu(i):
        print('第%s个异步进程' % i)
        print(threading.current_thread())

    def duoXianCheng(i):
        print('第%s个多线程' % i)
        print(threading.current_thread())

    start1 = time.time()
    for i in range(200):
        t = threading.Thread(target=duoXianCheng, args=(i,))
        t.start()
        t.join()
    end1 = time.time()

    start2 = time.time()
    loop = asyncio.get_event_loop()
    tasks = [yiBu(i) for i in range(200)]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
    end2 = time.time()

    print('\n多线程时间%s' % (end1-start1))
    print('\n异步线程时间%s' % (end2-start2))
