#!/usr/bin/env python
# -*- coding:utf-8 -*-

from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time

def hex_to_str(s):
    return ''.join([chr(i) for i in [int(b, 16) for b in s.split(' ')]])

driver = webdriver.Chrome()
driver.get("https://authzui.alipay.com/login/index.htm")
login_windows = driver.current_window_handle
try:
    time.sleep(5)
    status = driver.find_element_by_xpath('//ul[@id="J-loginMethod-tabs"]/li[@data-status="show_login"]')
    # page1 = driver.page_source
    # print(page1)
    time.sleep(1)
    status.click()
    time.sleep(5)
    element = WebDriverWait(driver, 10, 1).until(
        EC.presence_of_element_located((By.ID, "J-input-user"))
    )

    pe = WebDriverWait(driver, 10, 1).until(
        EC.presence_of_element_located((By.ID, "password_rsainput"))
    )

    login_btn = WebDriverWait(driver, 10, 1).until(
        EC.presence_of_element_located((By.ID, "J-login-btn"))
    )
    print(driver.get_network_conditions())
    if element and pe and login_btn:
        element.click()
        time.sleep(1)
        element.send_keys("15393112460")  # 参数为您的支付宝帐号
        time.sleep(5)
        pe.click()
        keys = hex_to_str('77 61 6e 31 33 31 34 5a 4e')
        pe.send_keys(keys)  # 在此输入您的支付宝密码
        time.sleep(5)
        # login_btn.send_keys(Keys.ENTER)
        login_btn.click()
        time.sleep(5)
        keys = hex_to_str('77 61 6e 31 33 31 34 5a 4e')
        pe.send_keys(keys)  # 在此输入您的支付宝密码
        time.sleep(5)
        # login_btn.send_keys(Keys.ENTER)
        login_btn.click()

        driver.implicitly_wait(10)
        driver.switch_to.window(driver.current_window_handle)
        page2 = driver.page_source
        print(page2)
        time.sleep(5)
        login_el = driver.find_element_by_xpath('//a[@title="转账"]')
        login_el.click()
        driver.switch_to.window(driver.current_window_handle)
        time.sleep(3)
        search_key = driver.find_element_by_id('ipt-search-key')
        search_key.click()
        time.sleep(1)
        search_key.send_keys('15393112460')
        time.sleep(2)
        driver.find_element_by_id('forAmount').click()
        time.sleep(2)
        page = driver.get_network_conditions()
        print(page)

finally:
    print("something wrong!")

