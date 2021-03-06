#!/usr/bin/env python
# encoding:utf-8
# @author: lvhuayan
# @file: login_success_case.py
# @time: 2021/3/6 20:44
# @desc:
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import unittest
from common import set_driver, login


class LoginSuccessCase(unittest.TestCase):
    def setUp(self) -> None: #写入selenium初始化配置
        self.driver = set_driver.set_driver()

    def tearDown(self) -> None: #测试清理、浏览器关闭
        time.sleep(2)
        self.driver.quit()

    def test_login_1(self):
        '''case2 测试账号test01 newdream123是否正确登录'''
        login.login(self.driver, 'test01', 'newdream123')
        actual_result=self.driver.find_element(By.XPATH,'//span[@class="user-name"]').text
        self.assertEqual(actual_result,'测试人员1','test_login1用例执行失败')

    def test_login_2(self):
        '''case3 测试账号test02 newdream123是否正确登录'''
        login.login(self.driver, 'test02', 'newdream123')
        # actual_result=self.driver.find_element(By.XPATH,'//span[@class="user-name"]').text
        # self.assertEqual(actual_result,'测试人员1','test_login1用例执行失败')
        self.assertTrue(EC.text_to_be_present_in_element(By.XPATH,'//span[@class="user-name"]'),'测试人员2')

if __name__=='__main__':
    unittest.main()