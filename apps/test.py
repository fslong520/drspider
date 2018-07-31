
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 一个多线程跟多进程的测试 '

__author__ = 'fslong'


import asyncio
import multiprocessing
import random
import threading
import time
import traceback

import pyquery


async def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = await connect# connect是个异步对象，需要使用异步方法来调用:
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    await writer.drain()# 同样的writer也是
    while True:
        line = await reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()
'''
loop = asyncio.get_event_loop()
# 生成了一个任务池:
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
'''

async def testAsync(i):
    start=time.time()
    print('线程%s'%(i+1))
    #time.sleep(5*random.random())
    end=time.time()
    a=[]
    for i in range(random.randint(1,10)):
        r=await testAsyncIn(i)
        a.append(r)
    print('一个%s个返回值'%(len(a)))
    print('异步线程%s执行了%s秒'%(i+1,end-start))

async def testAsyncIn(i):
    start=time.time()
    print('\n内部线程%s\n'%(i+1))
    #time.sleep(5*random.random())
    end=time.time()
    print('内部异步线程%s执行了%s秒'%(i+1,end-start))
    return('测试')
startAll=time.time()
loop1 =asyncio.get_event_loop()
tasks=[testAsync(i) for i in range(20)]
loop1.run_until_complete(asyncio.wait(tasks))
#loop1.run_until_complete(asyncio.wait([wget('www.baidu.com')]))
loop1.close()
endAll=time.time()
print('20个异步线程总共执行了%s'%(endAll-startAll))
