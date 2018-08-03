#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 美拍 '

__author__ = 'fslong'


import time
import traceback
import os

import pyquery
import requests
import asyncio
import base64
from spider import Spider


class Meipai(Spider):
    def getTitlePic(self):
        '''# 美拍热门接口：
        self.url = 'http://www.meipai.com/home/hot_timeline'
        self.params = {'page': 1, 'count': 12}
        '''
        jsonData = self.downLoadJson(self.url, 'page'+str(1))
        print(jsonData)

    def getVideo(self):
        self.url='http://www.meipai.com/media/1019039407'
        req=requests.get(self.url,headers=self.headers)
        PQreq=pyquery.PyQuery(req.text)
        urlBase64=PQreq('.mp-h5-player-layer-video > video').attr('src')
        print(urlBase64)
        

if __name__ == '__main__':
    meipai = Meipai()
    meipai.getVideo()

