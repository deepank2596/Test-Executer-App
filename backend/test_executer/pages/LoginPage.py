from test_executer.appdriver.TestBase import BasePage
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep


class LoginPage (BasePage):

    USER_NAME= (By.NAME, "txtUsername")
    PASSWORD= (By.NAME, "txtPassword")
    LOGIN_BTN= (By.CSS_SELECTOR,"input#btnLogin")

    def launchApp(self,**kwargs):
        self.get(kwargs["url"])

    def login(self,**kwargs):
        self.send_keys(self.USER_NAME, kwargs["username"])
        self.send_keys(self.PASSWORD, kwargs["password"])
        self.click(self.LOGIN_BTN)

    def sleep(self, **kwargs):
        sleep(int(kwargs["seconds"]))
