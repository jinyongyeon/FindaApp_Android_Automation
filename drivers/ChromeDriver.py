
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from config.info import InFo


class ChromeWebDriver:
    info = InFo()

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--lang=ko_KR")

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
