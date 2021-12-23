from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class DenyReimbursement:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def select_deny_button(self):
        element: WebElement = self.driver.find_element(By.ID, "deny33")
        return element

    def select_manager_deny_comment_input(self):
        element: WebElement = self.driver.find_element(By.ID, "managerComment33")
        return element
