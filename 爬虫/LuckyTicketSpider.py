#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
from multiprocessing import Process, Queue
import threading
import requests
import demjson


class LuckyTicket(threading.Thread):
    def __init__(self, url, q):
        super(LuckyTicket, self).__init__()
        self.url = url
        self.q = q
        self.headers = {
            'Host': 'www.cwl.gov.cn',
            'Referer': 'http://www.cwl.gov.cn/kjxx/ssq/kjgg/',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
            'Cookie': 'Sites=_21; UniqueID=dAOdfomeKsvyhBxK1540797507147; _ga=GA1.3.572618050.1540797507; _gid=GA1.3.1923181654.1540797507; _gat_gtag_UA_113065506_1=1; 21_vq=16'
        }

    def run(self):
        print('线程开始了')
        self.get_info()
        print('线程结束了2')

    #def is_alive(self):
    #    return Process.is_alive(self)

    def get_info(self):
        html = requests.get(
            url=self.url,
            headers=self.headers).content
        json = demjson.decode(html)
        # print(json['result'])
        result = json['result']
        print('数据下载完成，开始解析..' + str(len(result)))
        for data in result:
            red = str(data['red']).replace(",", "|")
            self.q.put(data['code'] + '|' + data['date'] + '|' + red + '|' + data['blue'])
        print(self.q.qsize())


def main():
    year = ['2014', '2015', '2016', '2017', '2018']
    page = ['1', '2', '3', '4']
    q = Queue()
    url_list = []
    # 构造所有URL
    for y in year:
        for p in page:
            #http://www.cwl.gov.cn/kjxx/fc3d/kjgg/
            #http://www.cwl.gov.cn/kjxx/ssq/kjgg/
            #base_url = 'http://www.cwl.gov.cn/cwl_admin/kjxx/findDrawNotice?name=ssq&issueCount=&issueStart=&issueEnd=&dayStart=' + y + '-01-01&dayEnd=' + y + '-12-31&pageNo=' + p
            base_url = 'http://www.cwl.gov.cn/cwl_admin/kjxx/findDrawNotice?name=3d&issueCount=&issueStart=&issueEnd=&dayStart=' + y + '-01-01&dayEnd=' + y + '-12-31&pageNo=' + p
            url_list.append(base_url)
    # 保存进程
    Process_list = []
    # 创建并启动进程
    for url in url_list:
        print(url + "开始下载...")
        p = LuckyTicket(url, q)
        p.start()
        Process_list.append(p)
    print('开始加入线程')
    # 让主进程等待子进程执行完成
    for i in Process_list:
        #print("线程状态"+str(i.is_alive()))
        i.join()

    print('线程加入完成')
    while not q.empty():
        print(q.get())


if __name__ == "__main__":
    print("开始爬取数据...")
    start = time.time()
    main()
    print('[info]耗时：%s' % (time.time() - start))
