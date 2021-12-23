from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class EmployeeLogout:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def select_employee_logout_button(self):
        element: WebElement = self.driver.find_element(By.ID, "employee_logout_button")
        return element
