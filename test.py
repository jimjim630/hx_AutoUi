import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    appPackage='com.topcredit.app',
    appActivity='com.example.crypto_otc.MainActivity',
    noReset="true",
    # 无线键盘
    connectHardwareKeyboard="true"
)

appium_server_url = 'http://localhost:4723'
driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
# driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Battery"]')
# driver.click()
