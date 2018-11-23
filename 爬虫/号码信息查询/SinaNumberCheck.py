#!/usr/bin/env python
# -*- coding:utf-8 -*-
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
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': 'U_TRS1=00000044.b9d21e81.5af26587.6b2e206f; UOR=www.google.com,blog.sina.com.cn,; SINAGLOBAL=61.178.98.68_1525835144.547997; SGUID=1540885346302_2872243; lxlrttp=1541383354; SCF=AtM9cDj7Gl2zTa81ri2aCUjszBc4jIM8h9Gk4Ta42o1xx7V_E4txPd42d1dVA5YnRFC005GV_YiTH8heYoa0rek.; SUB=_2AkMsthsTdcPxrAFQkfkQyWLjbYlH-jyfY3LlAn7tJhMyAhgv7nsLqSVutBF-XBnY2wNCXvHWCfApL7MiQZcbhAMH; SUBP=0033WrSXqPxfM72wWs9jqgMF55529P9D9WhuNdVQfxQefBIGLDM6SB225JpV2heRe02pS0eX12WpMC4odcXt; Apache=172.16.138.139_1542614230.514900; ULV=1542614234797:33:4:2:172.16.138.139_1542614230.514900:1542614232211; ULOGIN_IMG=tc-ff7b65167754bf8504c14b7b7ccac38a06ca',
    'Host': 'login.sina.com.cn',
    'Origin': 'https://login.sina.com.cn',
    'Referer': 'https://login.sina.com.cn/signup/signup?entry=homepage',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}
url = 'https://login.sina.com.cn/signup/check_user.php'

textmod = {
    'name': '',
    'format': 'json',
    'from': 'mobile'}

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
           '13321319712',
           '13327684335',
           '13359311511',
           '13359319032',
           '13359402666',
           '13359408138',
           '13359408303',
           '13359411099',
           '13359421092',
           '13359434757',
           '13359436272',
           '13359455655',
           '13359469029',
           '13359476964',
           '13359480222',
           '13359481986',
           '13359483348',
           '13359492522',
           '13359493998',
           '13359494706',
           '13369312238',
           '13369313921',
           '13369314452',
           '13369319228',
           '13369405208',
           '13369408076',
           '13369440014',
           '13369440959',
           '13369444124',
           '13369446461',
           '13369447826',
           '13369455470',
           '13369455593',
           '13369461200',
           '13369462388',
           '13369467071',
           '13369469255',
           '13369490246',
           '13369493948',
           '13389330555',
           '13389331785',
           '13389338898',
           '13389401385',
           '13389409482',
           '13389425040',
           '13389445776',
           '13399313124',
           '13399315308',
           '13399315461',
           '13399317933',
           '13399318299',
           '13399396965',
           '13399460244',
           '13399464765',
           '13399469160',
           '13399469283',
           '15309312043',
           '15309411553',
           '15309430390',
           '15309476815',
           '15309481138',
           '15336011784',
           '15336089082',
           '15339310022',
           '15339310310',
           '15339318941',
           '15339319061',
           '15339406682',
           '15339448736',
           '15339827333',
           '15339829793',
           '15339838238',
           '15339848066',
           '15339852722',
           '15339864569',
           '15343600773',
           '15343603653',
           '15343606533',
           '15343614147',
           '15343617315',
           '15343628661',
           '15343659234',
           '15346776080',
           '15346901183',
           '15346959812'

           ]
for n in numbers:
    textmod = {
        'name': n,
        'format': 'json',
        'from': 'mobile'}
    textmod = parse.urlencode(textmod)
    response = requests.post(url=url, data=textmod, headers=header_dict)
    status = response.status_code
    r = response.content.decode()
    if r == '{"retcode":100000}':
        print(str(n) + ':新浪未注册用户')
    else:
        print(str(n) + ':新浪已注册用户')

# 输出内容(python3默认获取到的是16进制'bytes'类型数据 Unicode编码，如果如需可读输出则需decode解码成对应编码):b'\xe7\x99\xbb\xe5\xbd\x95\xe6\x88\x90\xe5\x8a\x9f'
# 输出内容:登录成功
