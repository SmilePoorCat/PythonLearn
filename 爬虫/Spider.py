#!/usr/bin/env python
# -*- coding:utf-8 -*-

# encoding=utf-8
from bs4 import BeautifulSoup
import socket
import urllib, requests
import re
import lxml
import zlib
from multiprocessing import Process, Queue


class MyCrawler:
    def __init__(self, seeds):
        # 初始化当前抓取的深度
        self.current_deepth = 1
        # 使用种子初始化url队列
        self.linkQuence = linkQuence()
        if isinstance(seeds, str):
            self.linkQuence.addUnvisitedUrl(seeds)
        if isinstance(seeds, list):
            for i in seeds:
                self.linkQuence.addUnvisitedUrl(i)
        print("Add the seeds url \"%s\" to the unvisited url list" % str(self.linkQuence.unVisited))

    # 抓取过程主函数
    def crawling(self, seeds, crawl_deepth, file_out):
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
                links = self.getHyperLinks(visitUrl, file_out)
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
    def getHyperLinks(self, url, file_out):
        links = []
        titles = []
        file = open(file_out, mode='a+', encoding="utf-8")
        data = self.getPageSource(url)
        if data[0] == "200":
            soup = BeautifulSoup(data[1], "lxml")
            a = soup.findAll("a", {"href": re.compile('^http|^/')})
            if soup.title:
                t = soup.title.string
            else:
                t = 'null'
            file.write(str(t)+","+str(url))
            for i in a:
                if i["href"].find("http://") != -1:
                    links.append(i["href"])
        file.close()
        return links

    # 获取网页源码
    def getPageSource(self, url, timeout=100, coding=None):
        try:
            socket.setdefaulttimeout(timeout)
            header = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
            }
            response = requests.get(url=url, headers=header)
            page = response.content
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


def main(seeds, crawl_deepth, file_out):

    craw = MyCrawler(seeds)
    craw.crawling(seeds, crawl_deepth, file_out)


if __name__ == "__main__":
    main(["http://www.sina.com.cn"], 2, 'test1.txt')
