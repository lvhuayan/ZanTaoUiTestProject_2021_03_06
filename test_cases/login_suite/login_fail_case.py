#!/usr/bin/env python
# encoding:utf-8
# @author: lvhuayan
# @file: login_fail_case.py
# @time: 2021/3/6 20:44
# @desc:

import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import unittest
from common import set_driver,login

class LoginFailCase(unittest.TestCase):
    def setUp(self) -> None: #写入selenium初始化配置
        self.driver=set_driver.set_driver()

    def tearDown(self) -> None: #测试清理、浏览器关闭
        time.sleep(2)
        self.driver.quit()

    def test_login_1(self):
        '''case1 测试账号账号正确、密码错误时是否能登录'''
        login.login(self.driver,'test01','newdream12')
        self.assertTrue(EC.alert_is_present())#判断页面上是否存在alert

    def test_login_2(self):
        '''case1 测试账号账号错误、密码正确时是否能登录'''
        login.login(self.driver,'test','newdream123')
        self.assertTrue(EC.alert_is_present())#判断页面上是否存在alert

    def test_login_3(self):
        '''case1 测试账号账号密码都错误时是否能登录'''
        login.login(self.driver,'test111','newdream123')
        self.assertTrue(EC.alert_is_present())#判断页面上是否存在alert

if __name__=='__main__':
    unittest.main()