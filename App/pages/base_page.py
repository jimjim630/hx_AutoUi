import functools

from appium.webdriver.webdriver import WebDriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from appium.options.android import UiAutomator2Options

from appium import webdriver
import os
import time


class BasePage:
    def __init__(self, driver: WebDriver = None):
        if driver:
            self.driver = driver
        else:
            capabilities = {
                "platformName": "Android",
                "automationName": 'uiautomator2',
                # adb shell "dumpsys window | grep mCurrent"  获取appPackage 和 appActivity
                "appPackage": "com.topcredit.app",
                "appActivity": "com.example.crypto_otc.MainActivity",
                "noReset": "true",
                "autoAcceptAlerts": "true",
                # "settings[waitForIdleTimeout]": 0,
                # "language": 'zh'
            }
            appium_server_url = 'http://127.0.0.1:4723'
            self.driver = webdriver.Remote(appium_server_url,
                                           options=UiAutomator2Options().load_capabilities(capabilities))
            self.driver.implicitly_wait(5)

    def hx_find_element(self, locator_type: object, locator_value: object) -> object:
        """
        :param locator_type:
        :param locator_value:
        :return:
        """
        if locator_type == "id":
            return self.driver.find_element(by=AppiumBy.ID, value=locator_value)
        elif locator_type == "xpath":
            return self.driver.find_element(by=AppiumBy.XPATH, value=locator_value)
        elif locator_type == "class_name":
            return self.driver.find_element(by=AppiumBy.CLASS_NAME, value=locator_value)
            # 可以根据需要添加更多的定位方式，如name、tag_name等
        raise ValueError("不支持的定位类型")

    def find_abil_id(self, value):
        return self.driver.find_element_by_accessibility_id(value)

    def click_element(self, by, ele=None):
        """
        :param by:
        :param ele:
        :return:
        """
        if ele:
            return self.driver.find_element(by, ele).click()
        else:
            return self.driver.find_element(*by).click()

    def send_element(self, by, ele=None, val=None):
        """
        :param val:
        :param by:
        :param ele:
        :return:
        """
        if ele:
            return self.driver.find_element(by, ele).send_keys(val)
        else:
            return self.driver.find_element(*by).send_keys(val)

    def find_android_uiautomator(self, ele):
        """
        通过android_uiautomator 查找
        :param ele:
        :return:
        """
        return self.driver.find_element_by_android_uiautomator(ele)

    def click_android_uiautomator(self, ele):
        """
        通过android_uiautomator 查找
        :param ele:
        :return:
        """
        return self.driver.find_element_by_android_uiautomator(ele).click()

    def swipe_screen(self, direction, s_x=None, e_x=None, s_y=None, e_y=None):
        # 获取屏幕尺寸
        size = self.driver.get_window_size()

        # 向下滑动，滑动一屏
        if direction == 1:
            width = size['width']
            start_x = width / 2
            height = size['height']
            start_y = height * 0.8
            stop_x = start_x
            stop_y = height * 0.3
            self.driver.swipe(start_x, start_y, stop_x, stop_y, duration=1000)

        # 向右滑动
        elif direction == 2:
            width = size['width']
            start_x = width * 0.8
            height = size['height']
            start_y = height / 2
            stop_x = width * 0.3
            stop_y = start_y
            self.driver.swipe(start_x, start_y, stop_x, stop_y, duration=1000)

        # 自定义滑动
        elif direction == 3:
            self.driver.swipe(start_x=s_x, start_y=s_y, end_x=e_x, end_y=e_y, duration=1000)

    def swipe_find_element(self, text, direction):
        """
        滑动查找封装
        :param text: 要查找到的值
        :param direction: 滑动方向 1，上下滑动  ，2向右滑动,3 自定义滑动
        :return:
        """
        while True:
            try:
                element = self.find_element(AppiumBy.XPATH, f'//*[contains(@text,"{text}")]')
                self.driver.implicitly_wait(5)
                # 找到元素，并返回元素
                return element
            except NoSuchElementException:
                page_source = self.driver.page_source

                BasePage().swipe_screen(direction=direction)

                self.driver.implicitly_wait(5)

                # 截取当前页面所有元素，如果页面页面没有变化时跳出循环
                if self.driver.page_source == page_source:
                    break
                    raise NoSuchElementException(f"未找到元素")

    def screenshot(self):
        """
        截图
        :return:
        """
        img_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + "//screenshot//"
        s_time = time.strftime("%Y%m%d%H%M", time.localtime(time.time()))
        screen_save_path = img_folder + s_time + ".png"
        self.driver.get_screenshot_as_file(screen_save_path)
