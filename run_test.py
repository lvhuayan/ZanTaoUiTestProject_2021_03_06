#!/usr/bin/env python
# encoding:utf-8
# @author: lvhuayan
# @file: run_test.py
# @time: 2021/3/6 20:38
# @desc:

import os
import time
import unittest
import HTMLTestRunner

current_path=os.path.dirname(__file__)
report_path=os.path.join(current_path,'report')
testcase_path=os.path.join(current_path,'test_cases')
html_path=os.path.join(report_path,'report%s.html'%time.strftime('%Y-%m-%d-%H-%M-%S'))

discover=unittest.defaultTestLoader.discover(start_dir=testcase_path,
                                             pattern='*_case.py',
                                             top_level_dir=testcase_path)
main_suite=unittest.TestSuite()
main_suite.addTest(discover)

with open(html_path,'wb') as file:
    html_runner=HTMLTestRunner.HTMLTestRunner(stream=file,
                                              title='禅道UI自动化测试项目',
                                              description='由自动化测试组完成，包含大部分功能的自动化')
    html_runner.run(main_suite)

