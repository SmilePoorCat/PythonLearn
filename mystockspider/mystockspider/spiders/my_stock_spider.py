#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 定义爬虫类
import time
import os
import scrapy

from mystockspider.items import StockItem


def handle_detail(self):
    pass


class MyStockSpider(scrapy.Spider):
    # 定义爬虫名称（命令行启动爬虫要用）
    name = 'mystockspider'

    # 定义起始 url
    start_urls = ['http://stock.10jqka.com.cn/']

    def parse(self, response):
        # 提取页面个股超链接
        a_list = response.xpath("//div[@id='rzrq']/table[@class='m-table']/tbody/tr/td[2]/a")

        # 遍历所有超链接
        for a in a_list:
            # 提取股票名称、下载数据的url
            gp_name = a.xpath("./text()").extract()[0]
            link = a.xpath("./@href").extract()[0]
            gp_id = link.split('/')[-2]
            print("gp_id : ", gp_id)

            # 以个股名称作为文件名称，建立或清空一下文件
            path = "./files/"
            file_name = path + gp_name + ".csv"
            if not os.path.exists(path):
                os.makedirs(path)
            with open(file_name, "w+"):
                pass

            # 针对每只个股发起爬取子链接的请求
            # 对子链接的处理交由download_data函数进行处理
            # meta = 转交子链接处理函数所处理的数据
            yield scrapy.Request(
                url=link,
                callback=self.handle_detail,
                meta={'page': 1, 'url_base': link, 'name': gp_name, 'id': gp_id}
            )

        # 处理个股子链接返回的响应

    def handle_detail(self,response):

        # 构造数据模型
        item = StockItem()
        item['name'] = response.meta['name']
        item['data'] = ""

        # 提取出所有行，然后逐行提取所有单元格中的数据
        # 将数据保存到数据模型
        tr_list = response.xpath("//table[@class='m-table']/tbody/tr")
        for tr in tr_list:
            # 提取所有单元格中的数据，以英文逗号连接
            text_list = tr.xpath("./td/text()").extract()
            onerow = ','.join([text.strip() for text in text_list])

            # 存储数据到item
            item['data'] += onerow + "\n"

        # 提交数据模型给pipeline处理
        yield item

        # 爬取个股分页数据，最多爬取3页
        response.meta['page'] += 1
        if response.meta['page'] > 3:
            # 不再提交新的请求,爬虫结束
            return

        # 组装个股分页数据url
        url_str = 'http://data.10jqka.com.cn/market/rzrqgg/code/' + response.meta['id'] + '/order/desc/page/' + str(
            response.meta['page']) + '/ajax/1/'
        print("url_str = ", url_str)

        # 稍事休息后，爬取下一页数据，仍交由当前函数处理
        time.sleep(1)
        yield scrapy.Request(
            url=url_str,
            callback=self.handle_detail,
            meta={'page': response.meta['page'], 'url_base': url_str, 'name': response.meta['name'],
                  'id': response.meta['id']}
        )
