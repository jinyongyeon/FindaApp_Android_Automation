from appium import webdriver
# from appium.webdriver.common.options import Options



class WebDriver:


    @classmethod
    def setUp(cls):
        desired_caps = {
            "appium:device": "R3CR50AG9MH",
            "platformName": "Android",
            "appium:ensureWebviewsHavePages" : True,
            "appium:nativeWebScreenshot": True,
            "appium:newCommandTimeout": 3600,
            "appium:connectHardwareKeyboard": True
            # 'appActivity': '.ui.splash.SplashActivity',
            # 'noReset': 'true'
            # "appPackage": "kr.co.finda.finda",
            # "appActivity": "kr.co.finda.finda.ui.main.MainActivity"
        }
        cls.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        return cls.driver


    @classmethod
    def tearDown(cls):
        cls.driver.quit()


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