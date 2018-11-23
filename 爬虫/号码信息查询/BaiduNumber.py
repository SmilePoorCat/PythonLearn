#!/usr/bin/env python
# -*- coding:utf-8 -*-

from selenium import webdriver
import time

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

driver = webdriver.Chrome()
driver.get(
    "https://passport.baidu.com/v2/?reg&tt=1542702073936&overseas=undefined&gid=C7BD8C5-07A6-42B1-B5ED-1A03501EE953&tpl=mn&u=https%3A%2F%2Fwww.baidu.com%2Fs%3Fwd%3Dselenium%2520browser%2520switch%26rsv_spt%3D1%26rsv_iqid%3D0xb0be0d1500035d17%26issp%3D1%26f%3D3%26rsv_bp%3D1%26rsv_idx%3D2%26ie%3Dutf-8%26rqlang%3Dcn%26tn%3Dbaiduhome_pg%26rsv_enter%3D1%26inputT%3D9601%26rsv_t%3D8573l6v0EM72JdhLYWt4DnBqqXDC2XR6oDbFsnby7fB2A0k6R5XJiFkytHY9SMpjYuTf%26oq%3Dselenium%252520script%252520%2525E8%2525AF%2525B7%2525E6%2525B1%252582%26rsv_pq%3Dff50eb2d0004bc73%26sug%3Dselenium%252520browser%26rsv_sug3%3D75%26rsv_sug1%3D44%26rsv_sug7%3D100%26rsv_n%3D1%26rsv_sug2%3D0%26prefixsug%3Dselenium%252520browser%252520switch%26rsp%3D0%26rsv_sug4%3D181554")
login_windows = driver.current_window_handle
try:
    time.sleep(3)
    for i in numbers:
        driver.refresh()
        phone = driver.find_element_by_xpath("//input[@id='TANGRAM__PSP_3__phone']")
        pwd = driver.find_element_by_xpath('//input[@id="TANGRAM__PSP_3__password"]')
        phone.click()
        time.sleep(1)
        phone.send_keys(i)
        time.sleep(1)
        pwd.click()
        time.sleep(1)
        flag = False
        try:
            driver.find_element_by_xpath('//div[contains(text(), "该手机已注册，可以通过密码或短信快捷登录。")]')
            flag = True
        except:
            flag = False
        if flag:
            print(str(i)+'号码已注册百度账号')
            driver.find_element_by_xpath('//div[@class="tang-pass-pop-confirmWidget"]//a[@class="close-btn" and position()=last()]').click()
        else:
            print(str(i)+'号码未注册百度账号')
        phone.clear()
finally:
    print("something wrong!")
