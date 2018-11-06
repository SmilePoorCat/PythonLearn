#!/usr/bin/env python
# -*- coding:utf-8 -*-

import scrapy

from ScrapySpider.items import ScrapyspiderItem, BiqugeItem


class FirstSpider(scrapy.Spider):
    name = "first"
    allowed_domains = ["dmoztools.net"]
    start_urls = [
        "http://www.dmoztools.net/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoztools.net/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
        for sel in response.xpath('//ul/li'):
            item = ScrapyspiderItem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['desc'] = sel.xpath('text()').extract()
            yield item


class BiqugeSpider(scrapy.Spider):
    name = "biquge"
    allowed_domains = ["www.biquge5200.cc"]
    start_urls = [
        "https://www.biquge5200.cc/",
    ]

    def parse(self, response):
        body = response.xpath('//body//a').extract()
        print(body)
        for sel in response.xpath('//body//a'):
            item = BiqugeItem()
            item['title'] = sel.xpath('text()').extract()
            item['link'] = sel.xpath('@href').extract()
            # item['desc'] = sel.xpath('text()').extract()
            yield item

