#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
from urllib import parse
import requests
###

###
from urllib3 import request

header_dict = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Cookie': 'cna=wclxE3fB40ACAT2yYkT8tcon; mobileSendTime=-1; credibleMobileSendTime=-1; ctuMobileSendTime=-1; riskMobileBankSendTime=-1; riskMobileAccoutSendTime=-1; riskMobileCreditSendTime=-1; riskCredibleMobileSendTime=-1; riskOriginalAccountMobileSendTime=-1; unicard1.vm="K1iSL1GNZcgswianp9+QUA=="; UM_distinctid=1672e9efe6c12e-0b2d82a31c6a7e-4313362-144000-1672e9efe6d557; _TRACERT_COOKIE__fullfill_ref=https://docs.open.alipay.com/api_3%01a316.b4005%01; session.cookieNameId=ALIPAYJSESSIONID; LoginForm=alipay_login_auth; alipay="K1iSL1GNZcgswianp9+QUABntXcJKB/N8yFrA0AHDOnsrP3e"; CLUB_ALIPAY_COM=2088802363766768; iw.userid="K1iSL1GNZcgswianp9+QUA=="; ali_apache_tracktmp="uid=2088802363766768"; JSESSIONID=F5C9F6EDC95F16F422B28513E16A852C; ssl_upgrade=0; spanner=GUpZNrtBHwrf8rKDhs69LOd8llle1v9+4EJoL7C0n0A=; ctoken=jRlM15RGv8Qh7vbT; zone=RZ13A; ALIPAYJSESSIONID=RZ13jMuXlYXvEdFFzbQfvypsAeoJGoauthRZ13GZ00; rtk=17Np0bQ1LQ4VojI/+7U8anwYlFaEWQ/F1IlVTUMwulteuMIVlNT',
    'Host': 'shenghuo.alipay.com',
    'Referer': 'https://shenghuo.alipay.com/send/payment/fill.htm?_pdType=adbhajcaccgejhgdaeih',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
}
url = 'https://shenghuo.alipay.com/transfer/getUserInfo.json'
timeSnap='?timeSnap=1542677455291'
ua='&ua=053n%2BqZ9mgNqgJnCG0WtMC3zbvMsMaxxr7be9s%3D%7CnOiH84v8ifCK8Yj8ivKB%2BVk%3D%7CneiHGXz6UeRW5k4rRCFbKE0iR91xwGfVb9m8HLw%3D%7Cmu6b9JHoWfRQzUPrUeeeLqMqusm%2FFLEKf9tQ33n1UNxv3nf5cBW1%7Cm%2B%2BT%2FGIRfgdwH2QLbvZL4Yvkkf6L7k7u%7CmOOM6Yws%7CmeWK74oq%7CluKW%2BWcCqR6pGqzRo9FnzGTVf9Rs3q8LpAi7H6PSdMZ2BLIaqwx%2BzWnVZc18y7kQvBO8zWbRYeNB8lXCfs1l5UHmQ%2BhM4UfjReNJ4UznTepO5krhhOuO60vr%7Cl%2BGOEGMMfxBkHGgUew98BX8QZBxqE3wHfglmEmocZQpxBHPTcw%3D%3D%7ClOyDHXjUZ9CgFr4arwmi0nzUaA1i%2FIfyiuWQ55s7VCdILUgnUy9XIlv7Ww%3D%3D%7Cle%2BAHnvXZNOjFb0ZrAqh0X%2FXaw5hFXoOcgpzBKQE%7CkuuEGn%2FTYNenEbkdqA6l1XvTbwplEGUZdgVqH2wbYhS0FA%3D%3D%7Ck%2BqFG37SYdamELgcqQ%2Bk1HrSbgtkEWQYdwRrHm0XYRm5GQ%3D%3D%7CkOmGGH3RYtWlE7sfqgyn13nRbQhnEmcbdAdoHW4SZRKyEg%3D%3D%7CkeiHGXzQY9SkEroeqw2m1njQbAlmE2YadQZpHGgcYBy8HA%3D%3D%7CjveYBmPPfMu7DaUBtBK5yWfPcxZ5DHkFahl2A3cAeASkBA%3D%3D%7Cj%2FaZB2LOfcq6DKQAtRO4yGbOchd4DXgEaxh3AnYMegKiAg%3D%3D%7CjPWaBGHNfsm5D6cDthC7y2XNcRR7DnsHaBt0AXUJdQ6uDg%3D%3D%7CjfSbBWDMf8i4DqYCtxG6ymTMcBV6D3oGaRp1AHUDeA%2BvDw%3D%3D%7CivOcAmfLeM%2B%2FCaEFsBa9zWPLdxJ9CH0Bbh1yB3IJcgGhAQ%3D%3D%7Ci%2FKdA2bKec6%2BCKAEsRe8zGLKdhN8CXwAbxxzBnAFdgysDA%3D%3D%7CiPGeAGXJes29C6MHshS%2Fz2HJdRB%2FCn8DbB9wBXMEfgqqCg%3D%3D%7CifCfAWTIe8y8CqIGsxW%2BzmDIdBF%2BAm0ecQRyCXEEpAQ%3D%7ChvyTDWjEd8CwBq4KvxmywmzEeB1yAW4bbRZqGbkZ%7Ch%2F2SDGnNas1E8UPzdcd2wWXDdMKnyLzTptCr168Prw%3D%3D%7ChPOA85zvgPWa7pntgvSM9pnhnfKI8J%2Frn%2BiH85zokf6I9JvulvmM%2B5Thl%2FiN%2BJfilvmM%2F5DkmPeD%2BJfjmfaC%2B5TgmPeD9Jvul%2FiN9VU%3D'
rdsToken='&rdsToken=iyX9iV1ApmyHIvdyno97by4yK0lbKHyI'
account='&account=15393112460'
userId='&userId='
_input_charset='&_input_charset=utf-8'
r='&r=1542677455292'
ctoken='&ctoken=jRlM15RGv8Qh7vbT'
_callback='&_callback=arale.cache.callbacks.jsonp2'


numbers = ['18119490505',
           '18189531563',
           '18189530120',
           ]
for n in numbers:
    t = time.time()
    snap = int(round(t * 1000));
    rTime=snap+1
    timeSnap='&timeSnap='+str(snap)
    r='&r='+str(rTime)
    account='&account='+str(n)

    final_url = url+timeSnap+ua+rdsToken+account+userId+_input_charset+r+ctoken+_callback

    response = requests.get(url=url, headers=header_dict)
    status = response.status_code
    r = response.content.decode()
    print(r)
    time.sleep(1)
# 输出内容(python3默认获取到的是16进制'bytes'类型数据 Unicode编码，如果如需可读输出则需decode解码成对应编码):b'\xe7\x99\xbb\xe5\xbd\x95\xe6\x88\x90\xe5\x8a\x9f'
# 输出内容:登录成功
