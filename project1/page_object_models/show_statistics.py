from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class ShowStatistics:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def select_employee_id_input(self):
        element: WebElement = self.driver.find_element(By.ID, "statistic_employee_id")
        return element

    def select_show_statistics_button(self):
        element: WebElement = self.driver.find_element(By.ID, "statistics_button")
        return element
