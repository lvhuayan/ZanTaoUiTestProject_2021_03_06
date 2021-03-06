#!/usr/bin/env python
# encoding:utf-8
# @author: lvhuayan
# @file: set_driver.py
# @time: 2021/3/6 21:47
# @desc:
import os
from selenium import webdriver


def set_driver():
    current_path = os.path.dirname(__file__)
    webdriver_path = os.path.join(current_path, '../webdriver/chromedriver.exe')
    driver = webdriver.Chrome(executable_path=webdriver_path)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get('http://47.107.178.45/zentao/www/index.php?m=user&f=login')
    return driver