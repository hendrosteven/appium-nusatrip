from appium import webdriver


class Driver:
    def getDriver(self):
        caps = {
            'platformName': 'Android',
            'automationName': 'UiAutomator2',
            'platformVersion': '10',
            'deviceName': 'emulator-5554',
            'appPackage': 'com.nusatrip.android',
            'appActivity': 'com.nusatrip.MainActivity'
        }
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
        return driver
