import os

def start_appium_server():
    appium_command = "appium -a 127.0.0.1 -p 4723 -pa /wd/hub"
    os.system(appium_command)

if __name__ == "__main__":
    start_appium_server()