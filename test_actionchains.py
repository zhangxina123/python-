import os

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
import time

from selenium.webdriver.common.keys import Keys


class TestActionchains():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    # # 控制是否采用无界面形式运行自动化测试
    #     try:
    #         using_headless=os.environ["using_headless"]
    #     except KeyError:
    #         using_headless=None
    #         print("没有配置环境变量using_headless，按照有界面方式运行自动化测试")
    #     chrome_options=Options()
    #     if using_headless is not None and using_headless.lower()=='true':
    #         print('使用无界面方式运行')
    #         chrome_options.add_argument("--headless")

    def teardown(self):
        self.driver.quit()

    def test_case_click(self):
        self.driver.get('https://www.baidu.com/')
        self.driver.find_element_by_id('kw').send_keys('111111111')
        element_click = self.driver.find_element_by_id('su')
        action = ActionChains(self.driver)
        action.click(element_click)
        action.perform()

    def test_movetoelement(self):
        self.driver.get('https://www.baidu.com/')
        element_moveto = self.driver.find_element_by_id('s-usersetting-top')
        action = ActionChains(self.driver)
        action.move_to_element(element_moveto)
        action.perform()
        print("hello world")

    def test_dragdrop(self):
        self.driver.get(
            'https://passport.ctrip.com/user/login?backurl=https%3A%2F%2Fmy.ctrip.com%2Fmyinfo%2Fall&responsemethod=GET')
        drag_element = self.driver.find_element_by_xpath('//*[@id="sliderddnormal"]/div[1]/div[2]/div/i[1]')
        drop_element = self.driver.find_element_by_id('sliderddnormal')
        action = ActionChains(self.driver)
        action.drag_and_drop(drag_element, drop_element).perform()
        time.sleep(5)
        print("这是拖拽滑块滑动")

    def testkeys(self):
        self.driver.get(
            'https://passport.ctrip.com/user/login?backurl=https%3A%2F%2Fmy.ctrip.com%2Fmyinfo%2Fall&responsemethod=GET')
        self.driver.find_element_by_id('nloginname').send_keys('username zhang')
        time.sleep(3)
        action = ActionChains(self.driver)
        action.send_keys(Keys.BACK_SPACE)
        time.sleep(3)
        action.perform()
        time.sleep(3)
