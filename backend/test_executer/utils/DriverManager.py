from selenium import webdriver
from test_executer.config import DRIVER_PATH


def getDriver():
    web_driver= webdriver.Chrome(executable_path=DRIVER_PATH)
    web_driver.maximize_window()
    return web_driver



