#!/usr/bin/env python
# -*- coding:utf-8 -*-
# encoding=utf-8
from bs4 import BeautifulSoup
import socket
import urllib, requests
import re
import lxml
import zlib
import threading
from multiprocessing import Process, Queue
import time


class MyCrawler(threading.Thread):
    def __init__(self, seeds,crawl_deepth, q, linkQuence):
        super(MyCrawler, self).__init__()
        #加入结果队列
        self.q = q
        self.seeds = seeds
        self.crawl_deepth = crawl_deepth
        # 初始化当前抓取的深度
        self.current_deepth = 1
        # 使用种子初始化url队列
        self.linkQuence = linkQuence
        if isinstance(seeds, str):
            self.linkQuence.addUnvisitedUrl(seeds)
        if isinstance(seeds, list):
            for i in seeds:
                self.linkQuence.addUnvisitedUrl(i)
        print("Add the seeds url \"%s\" to the unvisited url list" % str(self.linkQuence.unVisited))

    # 多线程下载
    def run(self):
        self.crawling(self.seeds,self.crawl_deepth)

    # 抓取过程主函数
    def crawling(self, seeds, crawl_deepth):
        # 循环条件：抓取深度不超过crawl_deepth
        while self.current_deepth <= crawl_deepth:
            # 循环条件：待抓取的链接不空
            while not self.linkQuence.unVisitedUrlsEnmpy():
                # 队头url出队列
                visitUrl = self.linkQuence.unVisitedUrlDeQuence()
                print("Pop out one url \"%s\" from unvisited url list" % visitUrl)
                if visitUrl is None or visitUrl == "":
                    continue
                # 获取超链接
                links = self.getHyperLinks(visitUrl)
                # titles = linksAndTitle[1]
                print("Get %d new links" % len(links))
                # print("Links'Title is %d " % len(titles))
                # 将url放入已访问的url中
                self.linkQuence.addVisitedUrl(visitUrl)
                print("Visited url count: " + str(self.linkQuence.getVisitedUrlCount()))
                print("Visited deepth: " + str(self.current_deepth))
            # 未访问的url入列
            for link in links:
                self.linkQuence.addUnvisitedUrl(link)
            print("%d unvisited links:" % len(self.linkQuence.getUnvisitedUrl()))
            self.current_deepth += 1

    # 获取源码中得超链接
    def getHyperLinks(self, url):
        links = []
        data = self.getPageSource(url)
        #print(data)
        if data[0] == "200":
            soup = BeautifulSoup(data[1], "lxml")
            #a = soup.findAll("a", {"href": re.compile('^http|^/')})
            if soup.title:
                t = soup.title.string
                t = t.strip()
            else:
                t = time.time()

            a = soup.findAll("a")
            f = open(t,'a+',encoding='utf-8')
            text = soup.get_text();
            f.write(text)
            f.close()

            self.q.put(str(url))
            for i in a:
                if 'href' in str(i):
                    #print(i)
                    if i["href"].find("http://") != -1:
                        links.append(i["href"])
                    else:
                        #print(url + i["href"])
                        links.append(url+i["href"])
            iframe = soup.findAll("iframe")
            for i in iframe:
                if 'src' in str(i):
                    #print(i)
                    if i["src"].find("http://") != -1:
                        links.append(i["src"])
                    else:
                        #print(url + i["href"])
                        links.append(url+i["src"])
        return links

    # 获取网页源码
    def getPageSource(self, url, timeout=100, coding=None):
        try:
            #socket.setdefaulttimeout(timeout)
            header = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
            }
            response = requests.get(url=url, headers=header, timeout=5)
            page = response.content
            content_type = response.headers.get('Content-Type')
            #status = str(response.headers.get('status'))
            #print(content_type,status)
            #if 'text/html' != content_type:
            #    return ['Other Files', None]
            # if response.headers.get('Content-Encoding') == 'gzip':
            #    page = zlib.decompress(page, zlib.MAX_WBITS | 16)

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


class linkQuence:
    def __init__(self):
        # 已访问的url集合
        self.visted = []
        # 待访问的url集合
        self.unVisited = []

    # 获取访问过的url队列
    def getVisitedUrl(self):
        return self.visted

    # 获取未访问的url队列
    def getUnvisitedUrl(self):
        return self.unVisited

    # 添加到访问过得url队列中
    def addVisitedUrl(self, url):
        self.visted.append(url)

    # 移除访问过得url
    def removeVisitedUrl(self, url):
        self.visted.remove(url)

    # 未访问过得url出队列
    def unVisitedUrlDeQuence(self):
        try:
            return self.unVisited.pop()
        except:
            return None

    # 保证每个url只被访问一次
    def addUnvisitedUrl(self, url):
        if url != "" and url not in self.visted and url not in self.unVisited:
            self.unVisited.insert(0, url)

    # 获得已访问的url数目
    def getVisitedUrlCount(self):
        return len(self.visted)

    # 获得未访问的url数目
    def getUnvistedUrlCount(self):
        return len(self.unVisited)

    # 判断未访问的url队列是否为空
    def unVisitedUrlsEnmpy(self):
        return len(self.unVisited) == 0


def main(seeds, crawl_deepth, file_out,linkQuence):
    q = Queue()
    # 保存进程
    Process_list = []
    # 创建并启动进程
    for i in range(3):
        p = MyCrawler(seeds,crawl_deepth, q, linkQuence)
        p.start()
        Process_list.append(p)

    # 让主进程等待子进程执行完成
    for i in Process_list:
        i.join()

    file = open(file_out, mode='a+', encoding="utf-8")
    while not q.empty():
        file.write(q.get()+"\n")
    file.close()
    #craw = MyCrawler(seeds)
    #craw.crawling(seeds, crawl_deepth, file_out)


if __name__ == "__main__":
    linkQuence = linkQuence()
    main(["http://www.gov.cn/"], 1, 'gov.txt',linkQuence)
