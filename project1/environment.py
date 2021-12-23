from behave.runner import Context
from selenium import webdriver
from page_object_models.login_page import LoginPage
from page_object_models.create_reimbursement_page import CreateReimbursementPage
from page_object_models.approve_reimbursement import ApproveReimbursement
from page_object_models.deny_reimbursement import DenyReimbursement
from page_object_models.employee_logout import EmployeeLogout
from page_object_models.manager_logout import ManagerLogout
from page_object_models.reject_login import RejectLogin
from page_object_models.show_statistics import ShowStatistics
from page_object_models.reject_create_reimbursement import RejectCreateReimbursement


def before_all(context: Context):
    context.driver = webdriver.Chrome("chromedriver.exe")
    context.login_page = LoginPage(context.driver)
    context.create_reimbursement_page = CreateReimbursementPage(context.driver)
    context.approve_reimbursement = ApproveReimbursement(context.driver)
    context.deny_reimbursement = DenyReimbursement(context.driver)
    context.employee_logout = EmployeeLogout(context.driver)
    context.manager_logout = ManagerLogout(context.driver)
    context.show_statistics = ShowStatistics(context.driver)
    context.reject_login = RejectLogin(context.driver)
    context.reject_create_reimbursement = RejectCreateReimbursement(context.driver)
    context.driver.implicitly_wait(2)


def after_all(context):
    context.driver.quit()
