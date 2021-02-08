from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By 
from time import sleep

class BasePage:

    def __init__(self,driver:webdriver):
        self.driver= driver
        self.wait= WebDriverWait(driver, 30)

    def get(self, url:str):
        self.driver.get(url)

    def closeBrowser(self):
        self.driver.close()
        self.driver.quit()

    def findElement(self,locator):
        return self.wait.until(
            EC.presence_of_element_located(locator)
        )

    def click(self,locator):
        self.findElement(locator).click()

    def send_keys(self,locator, text:str):
        self.findElement(locator).send_keys(text)
    
    
