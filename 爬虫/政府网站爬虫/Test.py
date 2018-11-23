#!/usr/bin/env python
# -*- coding:utf-8 -*-
# encoding=utf-8
from multiprocessing import Queue

import requests
from bs4 import BeautifulSoup
import re


class Test():
    def __init__(self, q):
        super(Test, self).__init__()
        #加入结果队列
        self.q = q

    # 获取源码中得超链接
    def getHyperLinks(self, url):
        links = []
        data = self.getPageSource(url)
        if data[0] == "200":
            soup = BeautifulSoup(data[1], "lxml")
            # a = soup.findAll("a", {"href": re.compile('^http|^/')})
            a = soup.findAll("a")

            for i in a:
                t = i.get_text()
                #print(i)
                url2 = ''
                print(i)
                if 'href' in str(i):
                    #print(i)
                    if i["href"].find("http://") != -1:
                        url2 = i["href"]
                    else:
                        url2 = url+i["href"]
                if t:
                    t = t.replace(' ', '').replace("\n", "")
                elif t.strip() == '' or not t:
                    continue
                self.q.put(t + "," + url2)

    # 获取网页源码
    def getPageSource(self, url, timeout=100, coding=None):
        try:
            header = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
            }
            response = requests.get(url=url, headers=header, timeout=5)
            page = response.content
            content_type = response.headers.get('Content-Type')

            if coding is None:
                coding = response.headers.get("charset")

            # 如果获取的网站编码为None
            if coding is None:
                page = response.content
            # 获取网站编码并转化为utf-8
            else:
                page = response.content()
                page = page.decode(coding).encode('utf-8')
            return ["200", page]
        except Exception as e:
            print(str(e))
            return [str(e), None]



if __name__ == "__main__":
    q = Queue()
    t = Test(q)
    t.getHyperLinks("http://www.gov.cn/")

    file = open("gov2.txt", mode='a+', encoding="utf-8")
    while not q.empty():
        file.write(q.get() + "\n")
    file.close()