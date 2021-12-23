from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class RejectCreateReimbursement:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def negative_amount_input(self):
        element: WebElement = self.driver.find_element(By.ID, "new_reimbursement_amount")
        return element

    def manager_id_input(self):
        element: WebElement = self.driver.find_element((By.ID, "new_reimbursement_manager_id"))
        return element