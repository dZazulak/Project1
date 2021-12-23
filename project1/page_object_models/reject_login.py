from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class RejectLogin:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def select_email_input(self):
        element: WebElement = self.driver.find_element(By.ID, "email")
        return element

    def select_password_input(self):
        element: WebElement = self.driver.find_element(By.ID, "passcode")
        return element

    def select_login_button(self):
        element: WebElement = self.driver.find_element(By.ID, "login_button")
        return element
