from appium import webdriver

from config.info import InFo


# from appium.webdriver.common.options import Options



# class WebDriver_B:
#     # desired_caps = {
#     #     "appium:device": InFo.devices,
#     #     "platformName": "Android",
#     #     "appium:ensureWebviewsHavePages": True,
#     #     "appium:nativeWebScreenshot": True,
#     #     "appium:newCommandTimeout": 3600,
#     #     "appium:connectHardwareKeyboard": True
#     #     # 'appActivity': '.ui.splash.SplashActivity',
#     #     # 'noReset': 'true',
#     #     # "appPackage": "kr.co.finda.finda"
#     #     # "appActivity": "kr.co.finda.finda.ui.main.MainActivity"
#     # }
#     #
#     # driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
#
#     driver = None
#     # def __init__(self):
#     #     self.driver = None
#     @classmethod
#     def start(cls):
#         desired_caps = {
#             "appium:device": "R3CR50AG9MH",
#             "platformName": "Android",
#             "appium:ensureWebviewsHavePages": True,
#             "appium:nativeWebScreenshot": True,
#             "appium:newCommandTimeout": 3600,
#             "appium:connectHardwareKeyboard": True,
#         }
#         # 앱 실행 시에만 해당 값을 설정
#         if cls.run_with_app:
#             desired_caps['appActivity'] = '.ui.splash.SplashActivity'
#             desired_caps['noReset'] = 'true'
#             desired_caps['appPackage'] = 'kr.co.finda.finda'
#
#         cls.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
#
#     @classmethod
#     def quit(cls):
#         if cls.driver is not None:
#             cls.driver.quit()
#             cls.driver = None
#
#     @classmethod
#     def set_run_with_app(cls, run_with_app):
#         cls.run_with_app = run_with_app

    # @classmethod
    # def android_Back(cls):
    #     if cls.driver is not None:
    #         cls.driver.press_keycode(4)

class WebDriver:

    desired_caps = {
        "appium:device": InFo.devices,
        "platformName": "Android",
        "appium:ensureWebviewsHavePages": True,
        "appium:nativeWebScreenshot": True,
        "appium:newCommandTimeout": 3600,
        "appium:connectHardwareKeyboard": True
        # 'appActivity': '.ui.splash.SplashActivity',
        # 'noReset': 'true',
        # "appPackage": "kr.co.finda.finda"
        # "appActivity": "kr.co.finda.finda.ui.main.MainActivity"
    }

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)


    # @classmethod
    # def setUpClass(cls):
    #     desired_caps = {
    #         "appium:device": "R3CR50AG9MH",
    #         "platformName": "Android",
    #         "appium:ensureWebviewsHavePages" : True,
    #         "appium:nativeWebScreenshot": True,
    #         "appium:newCommandTimeout": 3600,
    #         "appium:connectHardwareKeyboard": True,
    #         'appActivity': '.ui.splash.SplashActivity',
    #         'noReset': 'true'
    #         # "appPackage": "kr.co.finda.finda",
    #         # "appActivity": "kr.co.finda.finda.ui.main.MainActivity"
    #     }
    #     cls.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    #     return cls.driver
    #
    #
    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.quit()
    #     cls.print("티어다운실행됨")



    # @classmethod
    # def initialize(cls):
    #     if cls.driver is None:
    #         cls.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", cls.desired_caps)
    #     return cls.driver
    # desired_caps = {
    #     "appium:device": "R3CR50AG9MH",
    #     "platformName": "Android",
    #     "appium:ensureWebviewsHavePages" : True,
    #     "appium:nativeWebScreenshot": True,
    #     "appium:newCommandTimeout": 3600,
    #     "appium:connectHardwareKeyboard": True,
    #     # "appPackage": "kr.co.finda.finda.stg",
    #     # "appActivity": "MainActivity"
    # }
    # driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

    # adb shell am start -n "kr.co.finda.finda/.ui.splash.SplashActivity"