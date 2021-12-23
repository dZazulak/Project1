from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class ApproveReimbursement:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def select_approve_button(self):
        element: WebElement = self.driver.find_element(By.ID, "approve30")
        return element

    def select_manager_approve_comment_input(self):
        element: WebElement = self.driver.find_element(By.ID, "managerComment30")
        return element
