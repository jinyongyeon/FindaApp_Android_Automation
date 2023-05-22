
from drivers.aos_webdrivers import WebDriver
from testscript.login_testscript.logincase import JoIn

webdriver = WebDriver()
join = JoIn()
webdriver.setUp()

join.enter_Personal_Information()