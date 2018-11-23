#!/usr/bin/env python
# -*- coding:utf-8 -*-
from urllib import parse
import requests
###

###
from urllib3 import request

textmod={'token': 'cd29b2d1f894d294ae249f4bdb17d665',
        'passport': '15393112460'}
textmod = parse.urlencode(textmod)
#print(textmod)
#输出内容:user=admin&password=admin
header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
               'Referer':'https://passport.mafengwo.cn/regist-mobile.html',
               'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
               'Cookie':'PHPSESSID=1qt4erokohrss35ncbv1ovll56; mfw_uuid=5bed1440-b7ce-0b5c-ec15-4fb3f71e6f2f; _r=chinaz; _rp=a%3A2%3A%7Bs%3A1%3A%22p%22%3Bs%3A41%3A%22top.chinaz.com%2FHtml%2Fsite_mafengwo.cn.html%22%3Bs%3A1%3A%22t%22%3Bi%3A1542263872%3B%7D; oad_n=a%3A5%3A%7Bs%3A5%3A%22refer%22%3Bs%3A48%3A%22http%3A%2F%2Ftop.chinaz.com%2FHtml%2Fsite_mafengwo.cn.html%22%3Bs%3A2%3A%22hp%22%3Bs%3A14%3A%22top.chinaz.com%22%3Bs%3A3%3A%22oid%22%3Bi%3A1029%3Bs%3A2%3A%22dm%22%3Bs%3A15%3A%22www.mafengwo.cn%22%3Bs%3A2%3A%22ft%22%3Bs%3A19%3A%222018-11-15+14%3A37%3A52%22%3B%7D; __mfwlv=1542263872; __mfwvn=1; uva=s%3A175%3A%22a%3A4%3A%7Bs%3A13%3A%22host_pre_time%22%3Bs%3A10%3A%222018-11-15%22%3Bs%3A2%3A%22lt%22%3Bi%3A1542263872%3Bs%3A10%3A%22last_refer%22%3Bs%3A48%3A%22http%3A%2F%2Ftop.chinaz.com%2FHtml%2Fsite_mafengwo.cn.html%22%3Bs%3A5%3A%22rhost%22%3Bs%3A14%3A%22top.chinaz.com%22%3B%7D%22%3B; __mfwurd=a%3A3%3A%7Bs%3A6%3A%22f_time%22%3Bi%3A1542263872%3Bs%3A9%3A%22f_rdomain%22%3Bs%3A14%3A%22top.chinaz.com%22%3Bs%3A6%3A%22f_host%22%3Bs%3A3%3A%22www%22%3B%7D; __mfwuuid=5bed1440-b7ce-0b5c-ec15-4fb3f71e6f2f; UM_distinctid=16716171e2b444-0c412bcebd2ceb-4313362-144000-16716171e2c4c7; __mfwlt=1542263916'}
url='https://passport.mafengwo.cn/regist/'
url2='https://passport.mafengwo.cn/regist-mobile.html'

resp1 = requests.get(url=url2)
print(resp1.status_code)
response  = requests.post(url=url,data=textmod,headers=header_dict)
status = response.status_code
r = response.content.decode()
#print(status)
#print(r)


#输出内容(python3默认获取到的是16进制'bytes'类型数据 Unicode编码，如果如需可读输出则需decode解码成对应编码):b'\xe7\x99\xbb\xe5\xbd\x95\xe6\x88\x90\xe5\x8a\x9f'
#输出内容:登录成功