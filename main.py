from selenium.webdriver.firefox.options import Options
from appium import webdriver
from appium.options.android import UiAutomator2Options

options = Options()


def app():
    capabilities = {
        "platformName": "Android",
        # adb shell "dumpsys window | grep mCurrent"  获取appPackage 和 appActivity
        "appPackage": "com.foure.app",
        "appActivity": "com.example.crypto_otc.MainActivity",
        "noReset": "true",
        "autoAcceptAlerts": "true",
        # "settings[waitForIdleTimeout]": 0,
        # "language": 'zh'
    }
    appium_server_url = 'http://127.0.0.1:4723'
    driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
    driver.implicitly_wait(5)
    return driver


#
# if __name__ == "__main__":
#     driver = app()

