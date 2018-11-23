#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
from requests.packages import chardet
from selenium import webdriver

url = 'http://gs.189.cn/web/pay2/viewpaybankV7.action?accountNo=249935729&oweAmount=0&resultCode=0&servType=0&servNumber=&isPrepaidPHS=0&truecheckname=acc561d085bad1b582351b07f18d1819&seqid=noActivity&accessWay=0&joinType=0&isLocal=3&objType=4&areaCode=9999&desTinationID=number&redesTinationID=number&amount=30&srand=8910&recommonedCode=%BF%C9%B2%BB%CC%EE'
alipay = 'https://shenghuo.alipay.com/send/payment/fill.htm'
numbers = ['18119490505',
           '18189531563',
           '18189530120',
           '18919899893',
           '18919137195',
           '17393161266',
           '15379012166',
           '18189691573',
           '15339833813',
           '19994335861',
           '18093111020',
           '19993135862',
           '18919925466',
           '15393112460',
           '18193157050',
           '18119316236',
           '13369459189',
           '18919888040',
           '15393165516',
           '18993392017',
           '18294402261',
           ]
dict = {}
browser=webdriver.Chrome()
try:
    #for n in numbers:
    #    u = url.replace('number', n)
    #    browser.get(u)
    #    label = browser.find_element_by_class_name('user_info_box_info').find_element_by_xpath('//label[2]').text
    #    name = label[6:].replace('*','')
    #    if not name:
    #        name = '暂无此人'
    #    dict[n] = name
    browser.get(alipay)
    id = browser.find_element_by_id('ipt-search-key')
    print(id)
finally:
    browser.close()


#for key in dict.keys():
#    print(str(key)+"机主姓氏为："+str(dict.get(key)))