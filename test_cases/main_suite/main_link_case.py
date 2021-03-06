#!/usr/bin/env python
# encoding:utf-8
# @author: lvhuayan
# @file: main_link_case.py
# @time: 2021/3/6 21:02
# @desc:
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import unittest

current_path=os.path.dirname(__file__)
webdriver_path=os.path.join(current_path,'../../webdriver/chromedriver.exe')
class MainLinkCase(unittest.TestCase):
    def setUp(self) -> None: #写入selenium初始化配置
        self.driver = webdriver.Chrome(executable_path=webdriver_path)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get('http://47.107.178.45/zentao/www/index.php?m=user&f=login')

    def tearDown(self) -> None: #测试清理、浏览器关闭
        time.sleep(2)
        self.driver.quit()

    def test_my_link(self):
        '''case4测试我的地盘菜单能否正确链接'''
        self.driver.find_element(By.XPATH,'//input[@id="account"]').send_keys('test01')
        self.driver.find_element(By.XPATH,'//input[@name="password"]').send_keys('newdream123')
        self.driver.find_element(By.XPATH,'//button[@id="submit"]').click()
        self.driver.find_element(By.XPATH,'//li[@data-id="my"]').click()
        self.assertTrue(EC.title_is('我的地盘-禅道'))

    def test_product_link(self):
        '''case5测试产品菜单能否正确链接'''
        self.driver.find_element(By.XPATH,'//input[@id="account"]').send_keys('test01')
        self.driver.find_element(By.XPATH,'//input[@name="password"]').send_keys('newdream123')
        self.driver.find_element(By.XPATH,'//button[@id="submit"]').click()
        self.driver.find_element(By.XPATH,'//li[@data-id="product"]').click()
        self.assertTrue(EC.title_is('产品主页-禅道'))

    def test_project_link(self):
        '''case5测试项目菜单能否正确链接'''
        self.driver.find_element(By.XPATH,'//input[@id="account"]').send_keys('test01')
        self.driver.find_element(By.XPATH,'//input[@name="password"]').send_keys('newdream123')
        self.driver.find_element(By.XPATH,'//button[@id="submit"]').click()
        self.driver.find_element(By.XPATH,'//li[@data-id="project"]').click()
        self.assertTrue(EC.title_is('项目主页-禅道'))

if __name__=='__main__':
    unittest.main()