#!/usr/bin/env python
# encoding:utf-8
# @author: lvhuayan
# @file: login.py
# @time: 2021/3/6 22:07
# @desc:
from selenium.webdriver.common.by import By


def login(driver,username,password):
    driver.find_element(By.XPATH, '//input[@id="account"]').send_keys(username)
    driver.find_element(By.XPATH, '//input[@name="password"]').send_keys(password)
    driver.find_element(By.XPATH, '//button[@id="submit"]').click()