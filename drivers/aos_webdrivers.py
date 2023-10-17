from appium import webdriver

from config.info import InFo




class WebDriver:
    info = InFo()
    desired_caps = {
        "appium:device": info.devices,
        "platformName": "Android",
        "appium:ensureWebviewsHavePages": True,
        "appium:nativeWebScreenshot": True,
        "appium:newCommandTimeout": 3600,
        "appium:connectHardwareKeyboard": True,
        "autoGrantPermissions": True
    }

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)


