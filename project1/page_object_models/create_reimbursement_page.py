from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class CreateReimbursementPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def select_create_reimbursement_button(self):
        element: WebElement = self.driver.find_element(By.ID, "reimbursementButton")
        return element

    def select_managerId_input(self):
        element: WebElement = self.driver.find_element(By.ID, "new_reimbursement_manager_id")
        return element

    def select_amount_input(self):
        element: WebElement = self.driver.find_element(By.ID, "new_reimbursement_amount")
        return element

    def select_message_input(self):
        element: WebElement = self.driver.find_element(By.ID, "new_reimbursement_message")
        return element

    def select_submit_button(self):
        element: WebElement = self.driver.find_element(By.ID, "new_reimbursement_submit_button")
        return element
